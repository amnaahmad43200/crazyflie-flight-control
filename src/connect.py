import cflib.crtp
from cflib.crazyflie import Crazyflie


def on_connected(link_uri):
    print(f"Connected to Crazyflie at {link_uri}")


def main():
    # Initialize drivers
    cflib.crtp.init_drivers()

    # Create Crazyflie object
    cf = Crazyflie()

    # Add callback
    cf.connected.add_callback(on_connected)

    # Connect to drone
    cf.open_link("radio://0/80/2M/E7E7E7E7E7")

    input("Press Enter to disconnect...")
    cf.close_link()


if __name__ == "__main__":
    main()