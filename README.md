Crazyflie Flight Control \& Logging System

Overview



This project implements control, logging, and visualization for a Crazyflie drone using Python and the Crazyflie client library. It demonstrates autonomous flight execution, real-time telemetry logging, and data visualization, along with integration into a structured robotics workflow.



The system is organized into modular scripts covering:



Drone connection and initialization

Takeoff and basic flight control

Synchronized and asynchronous logging

Position tracking and visualization

Autonomous motion patterns

Features

Drone connectivity via Crazyradio

Basic flight control (takeoff, landing, movement)

Synchronous and asynchronous telemetry logging

Real-time position tracking (x, y, z)

Data visualization using plots

Autonomous box flight pattern

Modular and extensible architecture





Project Structure



crazyflie-flight-control/

│

├── src/

│   ├── connect.py

│   ├── takeoff.py

│   ├── logging\_sync.py

│   ├── logging\_async.py

│   ├── parameter\_control.py

│   ├── flight\_logging.py

│   └── box\_flight.py

│

│

├── results/

│   ├── plots/

│   └── screenshots/

│

└── docs/

&#x20;   └── internship\_report.pdf









\---



\## References



\- Crazyflie Official Documentation  

&#x20; https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/



\- Crazyflie Python Library (cflib)  

&#x20; https://github.com/bitcraze/crazyflie-lib-python



\- Crazyflie Firmware Repository  

&#x20; https://github.com/bitcraze/crazyflie-firmware



\- Crazyradio USB Dongle Documentation  

&#x20; https://www.bitcraze.io/documentation/hardware/crazyradio/



\- Motion Commander API  

&#x20; https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/api/motion\_commander/



\- Logging Framework (cflib logging)  

&#x20; https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/user-guides/logging/



\- ROS2 Integration (Crazyflie ROS2 examples)  

&#x20; https://github.com/IMRCLab/crazyflie\_ros2

