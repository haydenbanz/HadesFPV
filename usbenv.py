import os
import win32api
import win32file
import subprocess
import time
import threading
import tkinter as tk
from tkinter import messagebox, simpledialog
import pyotp
import qrcode


from dotenv import load_dotenv
load_dotenv()

# Define constants
EXPECTED_KEY = os.getenv("EXPECTED_KEY")
SECRET_KEY_FILE = "secret.key"
QR_CODE_FILE = "authenticator_qr.png"
ICON_FILE = "usb.ico"
USB_EXECUTABLE = "usb.exe"
PROVISIONING_NAME = os.getenv("PROVISIONING_NAME", "user@example.com")
ISSUER_NAME = os.getenv("ISSUER_NAME", "YourAppName")

def get_secret_key():
    """Retrieve the secret key from a file or generate a new one if it doesn't exist."""
    if os.path.isfile(SECRET_KEY_FILE):
        with open(SECRET_KEY_FILE, 'r') as file:
            secret = file.read().strip()
    else:
        secret = pyotp.random_base32()
        with open(SECRET_KEY_FILE, 'w') as file:
            file.write(secret)
        # Generate and save the QR code
        totp = pyotp.TOTP(secret)
        uri = totp.provisioning_uri(name="your_email@example.com", issuer_name="YourAppName")
        qr = qrcode.make(uri)
        qr.save(QR_CODE_FILE)
        print(f'QR Code saved as {QR_CODE_FILE}')
    return secret

class USBMonitorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('USB Key Monitor with MFA')
        self.geometry('300x250')
        self.configure(bg='#2e2e2e')  # Dark mode background color
        self.is_running = False

        # Set application icon
        self.iconbitmap(ICON_FILE)

        self.secret = get_secret_key()
        self.totp = pyotp.TOTP(self.secret)

        # Create widgets
        self.mfa_button = tk.Button(self, text='Start MFA Authentication', command=self.start_mfa, bg='#444444', fg='white')
        self.mfa_button.pack(pady=10)

        self.start_button = tk.Button(self, text='Start USB Monitoring', command=self.start_monitoring, state=tk.DISABLED, bg='#444444', fg='white')
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self, text='Stop Monitoring', command=self.stop_monitoring, state=tk.DISABLED, bg='#444444', fg='white')
        self.stop_button.pack(pady=10)

        self.power_up_button = tk.Button(self, text='Power Up', command=self.power_up, bg='#444444', fg='white')
        self.power_up_button.pack(pady=10)

    def start_mfa(self):
        user_input_otp = simpledialog.askstring("OTP Verification", "Enter the OTP from Google Authenticator:", parent=self)

        if self.totp.verify(user_input_otp):
            messagebox.showinfo("Success", "The OTP is valid!")
            self.start_button.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "The OTP is invalid. Please try again.")

    def get_usb_drives(self):
        """Get a list of USB drives."""
        usb_drives = []
        drives = win32api.GetLogicalDriveStrings().split('\000')[:-1]
        for drive in drives:
            if win32file.GetDriveType(drive) == win32file.DRIVE_REMOVABLE:
                usb_drives.append(drive)
        return usb_drives

    def check_usb_key(self, drive):
        """Check if the usb.key file exists and matches the expected key."""
        key_file_path = os.path.join(drive, 'usb.key')
        if os.path.isfile(key_file_path):
            with open(key_file_path, 'r') as file:
                key = file.read().strip()
                if key == EXPECTED_KEY:
                    return True
        return False

    def lock_computer(self):
        """Lock the computer."""
        subprocess.call('rundll32.exe user32.dll,LockWorkStation')

    def start_monitoring(self):
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.monitor_thread = threading.Thread(target=self.monitor_usb, daemon=True)
        self.monitor_thread.start()

    def stop_monitoring(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def monitor_usb(self):
        """Monitor USB drives for the key."""
        while self.is_running:
            usb_drives = self.get_usb_drives()
            if not usb_drives:
                print("No USB drives detected.")
            else:
                for drive in usb_drives:
                    print(f"Checking drive: {drive}")
                    if self.check_usb_key(drive):
                        print(f"USB key file is valid on drive {drive}. Locking the computer.")
                        self.lock_computer()
                        time.sleep(60)
                        break  # Exit the loop after locking the computer

            time.sleep(10)

    def power_up(self):
        """Run usb.exe from the USB drive."""
        usb_drives = self.get_usb_drives()
        for drive in usb_drives:
            executable_path = os.path.join(drive, USB_EXECUTABLE)
            if os.path.isfile(executable_path):
                subprocess.Popen(executable_path)
                messagebox.showinfo("Power Up", f"Running {USB_EXECUTABLE} from {drive}.")
                return
        messagebox.showerror("Error", f"{USB_EXECUTABLE} not found on any USB drive.")

if __name__ == "__main__":
    app = USBMonitorApp()
    app.mainloop()
