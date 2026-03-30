import time
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
    if int(value_str):
        deck_attached_event.set()


def move_box(scf):
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        print("Flying in box...")

        mc.forward(0.3)
        time.sleep(1)

        mc.left(0.3)
        time.sleep(1)

        mc.back(0.3)
        time.sleep(1)

        mc.right(0.3)
        time.sleep(1)


def main():
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

        scf.cf.param.add_update_callback(
            group="deck", name="bcFlow", cb=param_deck_flow
        )

        time.sleep(1)

        if not deck_attached_event.wait(timeout=5):
            print("No deck detected")
            return

        move_box(scf)


if __name__ == "__main__":
    main()