import os

import jwt

encoded = jwt.encode(
    {"test": "This is going to work great"}, os.environ.get("KEY"), algorithm="HS256"
)

string_encoded = encoded.decode()

decoded = jwt.decode(string_encoded.encode(), os.environ.get("KEY"), algorithms="HS256")

print(decoded)
