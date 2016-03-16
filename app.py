import notebook as nb
import json


# Default Variables
notebooks = []


def jdefault(o):
    return o.__dict__


def initialize():
    'loads the json dump to vaiables'
    jd = open('data.json', 'r')

    for ntb in jd.readlines():
        notebooks.append(nb.notebook(json.loads(ntb)['title']))


def finalize():
    'closes the apps, dumps the json'
    jd = open('data.json', 'w')

    for ntb in notebooks:
        jd.write(json.dumps(ntb, default=jdefault))


def parse(arg):
    'Parser for app console, returns note and notebook objects'
    arguments = arg.split()  # Split arguments

    if len(arguments):
        if arguments[0] == 'nnb' or arguments[0] == 'newnotebook':

            if len(arguments) == 1:
                notebooks.append(nb.notebook())

            else:
                notebooks.appned(nb.notebook(arguments[1]))

        if arguments[0] == 'nn' or arguments[0] == 'newnote':

            if len(arguments) == 1:
                nb.note()

            elif len(arguments) == 2:
                return nb.note(title=arguments[1])

            elif len(arguments) == 3:
                nb.note(title=arguments[1], node=arguments[2])

            elif len(arguments) == 4:
                nb.note(title=arguments[1], node=arguments[2])

        if arguments[0] == 'q' or arguments[0] == 'quit':
            break


if __name__ == "__main__":
    initialize()

    while True:
        parse(input('#>'))

    finalize()
