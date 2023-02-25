# https://docs.python.org/2/library/json.html

import json

dumps = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

print dumps

dumps_event_body = json.dumps("{\n    \"photo\": \"0007.png\"\n}")

print dumps_event_body


dumps_event_load = json.loads("{\n    \"photo\": \"0007.png\"\n}")

print type(dumps_event_load)

print dumps_event_load

print dumps_event_load['photo']