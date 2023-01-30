# Note
* flask does not support http2 -> use `quart` with `hypercorn`
* For the time being, I don't use the [Services](./Services/) package, all the functions are in `app.py` and the [crud](./crud/) . package


# Run
```sh
hypercorn --keyfile openssl/key.pem --certfile openssl/cert.pem --bind 'localhost:5000' app:app
```
Default: ```Enter PEM pass phrase: 0000```
# How to generate a self-signed certificate
You can do that in one command:

```sh
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365
```

You can also add -nodes (short for "no DES") if you don't want to protect your private key with a passphrase. Otherwise it will prompt you for "at least a 4 character" password.

The days parameter (365) you can replace with any number to affect the expiration date. It will then prompt you for things like "Country Name", but you can just hit Enter and accept the defaults.

Add -subj '/CN=localhost' to suppress questions about the contents of the certificate (replace localhost with your desired domain).