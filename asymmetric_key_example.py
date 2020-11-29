import datetime
import time

import jwt

with open("./key.pem") as priv_key_file:
    private_key_read = priv_key_file.readlines()
    private_key = bytes("".join(private_key_read), "utf-8")

with open("./public.pem") as public_key_file:
    public_key_read = public_key_file.readlines()
    public_key = bytes("".join(public_key_read), "utf-8")

generated_at = datetime.datetime.utcnow()

jwt_payload = {
    "aud": "edi.example.org",
    "exp": generated_at + datetime.timedelta(seconds=3),
    "iat": generated_at,
    "iss": "example.org:edi",
    "test": "This is going to work great",
}


encoded = jwt.encode(jwt_payload, private_key, algorithm="RS512")

string_encoded = encoded.decode()
print(string_encoded)

time.sleep(3)

try:
    decoded = jwt.decode(
        string_encoded.encode(),
        public_key,
        audience="edi.example.org",
        leeway=2,
        algorithms="RS512",
    )
    print(decoded)
except jwt.ExpiredSignatureError:
    print("signature has expired")
