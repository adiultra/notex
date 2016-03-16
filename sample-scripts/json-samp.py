import json


class note:
    def __init__(self, title='', body=''):
        self.title = title
        self.body = body

    def display(self):
        print('\nTitle :', self.title)
        print('\nBody :', self.body)

films = [
    [123, "I am cool"],
    [234, "You guessed it"]
]

g = note("What", "Do you mean")

f = open('data.json', 'w')


def jdefault(o):
    return o.__dict__

jdump = json.dumps(g, default=jdefault, indent=4)

f.write(jdump)
f.close()

f = open('data.json', 'r')
j = f.read()
obj = note(json.loads(j)['title'], json.loads(j)['body'])

obj.display()
