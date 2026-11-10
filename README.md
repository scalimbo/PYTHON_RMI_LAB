This project is for the midterm LAB of IT 120. Where it translates the referenced Java RMI into a python system

## FILES

- `product.py` - it remotely exposed 'Product' data object.
- `server.py` - starts the Pyro5 name server, registers four products, and
  waits for requests.
- `client.py` - looks up a product remotely and prints its details.
