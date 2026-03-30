import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.log import LogConfig
from cflib.utils import uri_helper


URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

logging.basicConfig(level=logging.ERROR)


def log_callback(timestamp, data, logconf):
    print(f"[{timestamp}] Roll={data['stabilizer.roll']:.2f}, "
          f"Pitch={data['stabilizer.pitch']:.2f}, "
          f"Yaw={data['stabilizer.yaw']:.2f}")


def main():
    cflib.crtp.init_drivers()

    log_config = LogConfig(name='Stabilizer', period_in_ms=100)
    log_config.add_variable('stabilizer.roll', 'float')
    log_config.add_variable('stabilizer.pitch', 'float')
    log_config.add_variable('stabilizer.yaw', 'float')

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        cf = scf.cf
        cf.log.add_config(log_config)
        log_config.data_received_cb.add_callback(log_callback)

        log_config.start()

        try:
            time.sleep(10)
        finally:
            log_config.stop()


if __name__ == "__main__":
    main()