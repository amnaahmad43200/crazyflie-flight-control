import time
import sys
from threading import Event

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper


URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')
DEFAULT_HEIGHT = 0.3

deck_attached_event = Event()


def param_deck_flow(_, value_str):
    value = int(value_str)
    if value:
        print("Deck detected")
        deck_attached_event.set()
    else:
        print("Deck NOT detected")


def takeoff(scf):
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        print("Taking off...")
        time.sleep(3)
        print("Landing...")


def main():
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        scf.cf.param.add_update_callback(
            group="deck", name="bcFlow", cb=param_deck_flow
        )

        time.sleep(1)

        if not deck_attached_event.wait(timeout=5):
            print("No flow deck detected. Exiting.")
            sys.exit(1)

        takeoff(scf)


if __name__ == "__main__":
    main()