import base64
import json
import pprint

payload = input("paste payload here: ")
decoded_bytes = base64.b64decode(payload)
decoded_string = decoded_bytes.decode('utf-8')
json_object = json.loads(decoded_string)
pprint.pprint(json_object)

