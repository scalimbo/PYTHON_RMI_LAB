This project is for the midterm LAB of IT 120. Where it translates the referenced Java RMI into a python system

## FILES

- `product.py` - it remotely exposed 'Product' data object.
- `server.py` - starts the Pyro5 name server, registers four products, and
  waits for requests.
- `client.py` - looks up a product remotely and prints its details.

## Run on Windows

Open two PowerShell terminals in this folder by clicking on the Terminal tab above the viewport or pressing Cntrl+Shift+`.

### Terminal 1: start the server

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe server.py
```

Keep this terminal running. It should be able to report that `laptop`, `mobile`, `bag`,
and `charger` are registered.

### Terminal 2: run the client

```powershell
.\.venv\Scripts\python.exe client.py
```

The default lookup is `laptop`. To call another registered remote object:

```powershell
.\.venv\Scripts\python.exe client.py --product charger
```

Expected output for the default client:

```text
Name: Laptop
Description: Lenovo laptop
Price: 800000.0
```

Stop the server with `Ctrl+C`
