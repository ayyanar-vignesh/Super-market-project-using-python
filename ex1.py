import json 

# url="http://dummydata.com"

url='{"order":"dhosa","quantity":5}'
print(type(url))

y=json.loads(url)
print(y["order"])

print(y["quantity"])
