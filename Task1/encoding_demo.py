import base64
import urllib.parse
import hashlib

message = "Hello, Softwarica!"
b64_encoded = base64.b64encode(message.encode()).decode()
print("Original:      " + message)
print("Base64 Encoded: " + b64_encoded)
print("Base64 Decoded: " + base64.b64decode(b64_encoded).decode())

url_param = "student name=Asha Sharma&city=Kathmandu"
url_encoded = urllib.parse.quote(url_param)
print("URL Encoded:   " + url_encoded)

data = "SecretData"
hex_out = data.encode().hex()
print("Hex Encoded:   " + hex_out)

h = hashlib.sha256(message.encode()).hexdigest()
print("SHA-256 Hash:  " + h)