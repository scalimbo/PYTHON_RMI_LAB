import threading

from Pyro5.api import Daemon, locate_ns, start_ns
from sympy import Product

HOST = "127.0.0.1"
NAMESERVER_PORT = 9090

def main() -> None:
    print("Server is booting up...")

    _, nameserverdaemon, broadcastserver = start_ns(host=HOST, port=NAMESERVER_PORT)
    nameserver_thread = threading.Thread(target=nameserverdaemon.requestLoop,name="pyro-nameserver", daemon=True,)
    nameserver_thread.start()
    nameserver = locate_ns(host=HOST, port=NAMESERVER_PORT)

    products = {
        "laptop": Product("Laptop", "Lenovo laptop", 800000.0),
        "mobile": Product("Mobile", "Apple iPhone", 70000.0), 
        "bag": Product("Bag", "Leather bag", 5000.0),
        "charger": Product("Charger", "Fast charger", 2000.0),
        }

        with Daemon(host=HOST) as daemon:
            for name, product in products.items():
                uri = daemon.regeister(product)
                nameserver.register(name, uri)

            print("Name server: {HOST}:{NAMESERVER_PORT}")
            print("Registered products: " + ",".join(products))
            print("Waiting for clients requests. Press Cntrl+C to exit.")

            try:
                daemon.requestLoop()
            except KeyboardInterrupt:
                print("Server is shutting down...")
            finally:
                nameserver.remove(name)
                nameserverdaemon.shutdown()
                broadcast_server.close()


if __name__ == "__main__":
    main()
    