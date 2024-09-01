drone_project/
│
├── drone/
│   ├── __init__.py
│   ├── main.py
│   ├── motor_control.py
│   ├── sensor_reading.py
│   ├── telemetry.py
│   ├── config/
│   │   ├── config.json
│   │   └── motor_config.json
│   └── logs/
│       └── drone_log.log
│
├── remote_control/
│   ├── __init__.py
│   ├── remote_main.py
│   ├── remote_control.py
│   ├── config/
│   │   └── remote_config.json
│   └── logs/
│       └── remote_log.log
│
├── documentation/
│   ├── README.md
│   ├── INSTALLATION.md
│   ├── USAGE.md
│   └── DESIGN.md
│
├── tools/
│   ├── __init__.py
│   ├── mavproxy_setup.py
│   └── network_setup.py
│
└── tests/
    ├── __init__.py
    ├── test_motor_control.py
    ├── test_sensor_reading.py
    ├── test_telemetry.py
    ├── test_remote_control.py
    └── test_mavproxy_setup.py
