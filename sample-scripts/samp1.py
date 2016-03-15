import json


class note:
    def __init__(self, title='', body=''):
        self.title = title
        self.body = body

films = [
    [123, "I am cool"],
    [234, "You guessed it"]
]

g = note("What", "Do you mean")


def jdefault(o):
    return o.__dict__

print(json.dumps(films, indent=4))
print(json.dumps(g, default=jdefault))

jdump = json.dumps(g, default=jdefault)

obj = note(json.loads(jdump)['title'], json.loads(jdump)['body'])

print(obj.body)
