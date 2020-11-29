from uuid import uuid4

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

RSA_STANDARD = 65537

new_key_id = str(uuid4())

private_key = rsa.generate_private_key(public_exponent=RSA_STANDARD, key_size=4096)
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption(),
)

print(private_pem.decode())

with open(f"./{new_key_id}-private.pem", "w") as priv_key_file:
    priv_key_file.write(private_pem.decode())

public_key = private_key.public_key()

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

with open(f"./{new_key_id}-public.pem", "w") as pub_key_file:
    pub_key_file.write(public_pem.decode())
