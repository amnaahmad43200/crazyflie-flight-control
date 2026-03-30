import logging
import sys
import time
from threading import Event

import matplotlib.pyplot as plt

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper


URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')
DEFAULT_HEIGHT = 0.3

deck_attached_event = Event()

logging.basicConfig(level=logging.ERROR)

# Data storage
t, x, y, z = [], [], [], []


def param_deck_flow(_, value_str):
    if int(value_str):
        deck_attached_event.set()


def log_callback(timestamp, data, logconf):
    t.append(timestamp)
    x.append(data['stateEstimate.x'])
    y.append(data['stateEstimate.y'])
    z.append(data['stateEstimate.z'])


def main():
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

        log_config = LogConfig(name='Position', period_in_ms=50)
        log_config.add_variable('stateEstimate.x', 'float')
        log_config.add_variable('stateEstimate.y', 'float')
        log_config.add_variable('stateEstimate.z', 'float')

        scf.cf.log.add_config(log_config)
        log_config.data_received_cb.add_callback(log_callback)

        scf.cf.param.add_update_callback(group="deck", name="bcFlow", cb=param_deck_flow)

        time.sleep(1)

        if not deck_attached_event.wait(timeout=5):
            print("No flow deck detected")
            sys.exit(1)

        log_config.start()

        with MotionCommander(scf, default_height=DEFAULT_HEIGHT):
            print("Flying...")
            time.sleep(5)

        log_config.stop()

    # Plot results
    plt.figure()
    plt.plot(t, x)
    plt.title("X Position")

    plt.figure()
    plt.plot(t, y)
    plt.title("Y Position")

    plt.figure()
    plt.plot(t, z)
    plt.title("Z Position")

    plt.show()


if __name__ == "__main__":
    main()