# https://docs.python.org/2/library/json.html
# https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html

import json

dumps = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

print dumps

dumps_event_body = json.dumps("{\n    \"photo\": \"0007.png\"\n}")

print dumps_event_body


dumps_event_load = json.loads("{\n    \"photo\": \"0007.png\"\n}")

print type(dumps_event_load)

print dumps_event_load

print dumps_event_load['photo']


dic_response = {"version": "2.0", "routeKey": "$default", "rawPath": "/", "rawQueryString": "", "headers": {"content-length": "27", "x-amzn-tls-version": "TLSv1.2", "x-forwarded-proto": "https", "postman-token": "309182f7-9b4d-406a-8f8c-7e4a2cd4f43a", "x-forwarded-port": "443", "x-forwarded-for": "54.86.50.139", "accept": "*/*", "x-amzn-tls-cipher-suite": "ECDHE-RSA-AES128-GCM-SHA256", "x-amzn-trace-id": "Root=1-63fa8185-4c7513c5647c42e4267fa6d6", "host": "bv4ztnh4x5y4uo7lziofomqtfe0fscwo.lambda-url.us-east-1.on.aws", "content-type": "application/json", "cache-control": "no-cache", "accept-encoding": "gzip, deflate, br", "user-agent": "PostmanRuntime/7.31.1"}, "requestContext": {"accountId": "anonymous", "apiId": "bv4ztnh4x5y4uo7lziofomqtfe0fscwo", "domainName": "bv4ztnh4x5y4uo7lziofomqtfe0fscwo.lambda-url.us-east-1.on.aws", "domainPrefix": "bv4ztnh4x5y4uo7lziofomqtfe0fscwo", "http": {"method": "GET", "path": "/", "protocol": "HTTP/1.1", "sourceIp": "54.86.50.139", "userAgent": "PostmanRuntime/7.31.1"}, "requestId": "a6fd1296-b319-4702-b900-4e9a189d57b4", "routeKey": "$default", "stage": "$default", "time": "25/Feb/2023:21:45:41 +0000", "timeEpoch": 1677361541050}, "body": "{\n    \"photo\": \"0007.png\"\n}", "isBase64Encoded": False}

print type(dic_response)

print dic_response['version']

print dic_response['headers']

json_load_body = json.loads(dic_response['body'])
print json_load_body
print json_load_body['photo']