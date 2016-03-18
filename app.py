from functions import jdefault
import notebook as nb
import json


# Default Variables
notebooks = []

# load json data for notebooks
jd = open('data.json', 'r')


def initialize():
    for ntb in jd.readlines():
        jntb = json.loads(ntb)
        append_ntb = nb.notebook(jntb['title'])
        append_ntb.notelist = jntb['notelist']
        notebooks.append(append_ntb)


def finalize():
    'closes the apps, dumps the json'
    jd = open('data.json', 'w')

    for ntb in notebooks:
        jd.writeline(json.dumps(ntb, default=jdefault))


def opennb(title):
    for ntb in notebooks:
        if ntb.title == title:
            print(ntb.title)
            return ntb
            break


def parse(arg):
    'Parser for app console, returns note and notebook objects'
    arguments = arg.split()  # Split arguments

    if len(arguments):
        if arguments[0] == 'onb' or arguments[0] == 'opennotebook':
            if len(arguments) == 2:
                onb = opennb(arguments[1])

        if arguments[0] == 'nnb' or arguments[0] == 'newnotebook':

            if len(arguments) == 1:
                notebooks.append(nb.notebook(node=onb.title))

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

    while True:
        parse(input('#>'))

    finalize()
