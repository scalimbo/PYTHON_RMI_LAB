import threading

from Pyro5.api import Daemon, locate_ns, start_ns

HOST = "127.0.0.1"
NAMESERVER_PORT = 9090

def main() -> None:
    print("Server is booting up...")

    