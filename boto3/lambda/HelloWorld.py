import json

print('Loading function')


def lambda_handler(event, context):
    resp = f"Hi, {event['name']}! How are you?"
    return resp


"""
Example event JSON:

{
  "name":"Gergely"
}
"""