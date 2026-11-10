import argparse

from Pyro5.api import Proxy, locate_ns

HOST = "127.0.0.1"
NAMESERVER_PORT = 9090

def main() -> None:
    parser = argparse.ArgumentParser(description="Read a product through Pyro5.")
    parser.add_argument(
        "--product",
        default="laptop",
        choices=("laptop", "mobile", "bag", "charger"),
        help="registered product name (default: laptop)",
    )
    args = parser.parse_args()

    nameserver = locate_ns(host=HOST, port=NAMESERVER_PORT)
    product_uri = nameserver.lookup(args.product)

    with Proxy(product_uri) as product:
        print(f"Name: {product.get_name()}")
        print(f"Description: {product.get_description()}")
        print(f"Price: ${product.get_price():.2f}")

if __name__ == "__main__":
    main()