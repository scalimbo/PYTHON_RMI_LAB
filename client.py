import argparse

from Pyro5.api import Proxy, locate_ns

HOST = "127.0.0.1"

def main() -> None:
    parser = argparse.ArgumentParser(description="Read a product throgh Pyro5.")