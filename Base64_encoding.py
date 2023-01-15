#Damian Wyrwinski 79818 15/01/2023
import base64

sample_string = "Test"
sample_string_bytes = sample_string.encode("ascii")

base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")

print(f"Zaszyfrowana wiadmość: {base64_string}")
