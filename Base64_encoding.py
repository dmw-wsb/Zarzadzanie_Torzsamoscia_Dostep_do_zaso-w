#Damian Wyrwinski 79818 15/01/2023
import base64

base64_string = "VGVzdA=="
base64_bytes = base64_string.encode("ascii")

sample_string_bytes = base64.b64decode(base64_bytes)
sample_string = sample_string_bytes.decode("ascii")

print(f"Rozszyfrowana wiadomość to: {sample_string}")
