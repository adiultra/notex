import json


class note:
    def __init__(self, title='', body=''):
        self.title = title
        self.body = body
        self.array = [1, 2, 3, 4]

    def display(self):
        print('\nTitle :', self.title)
        print('\nBody :', self.body)

    def aray(self):
        for i in self.array:
            print(i+1)

films = [
    [123, "I am cool"],
    [234, "You guessed it"]
]

g = note("What", "Do you mean")
# g2 = note("Why", 'can\'t you wait')
f = open('data.json', 'w')


def jdefault(o):
    return o.__dict__

jdump = json.dumps(g, default=jdefault)
# jdump += '\n' + json.dumps(g2, default=jdefault)

f.write(jdump)
f.close()

f = open('data.json', 'r')
j = f.readline()
print(j)
obj = note(json.loads(j)['title'], json.loads(j)['body'])

obj.display()
obj.aray()
# j = f.readline()
# obj = note(json.loads(j)['title'], json.loads(j)['body'])
# obj.display()
# f.close()
