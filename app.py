from functions import jdefault
import notebook as nb
import json


manual = """Notex
The Note taking app
------------------

help    : This command displays the following help

commands :

    lnb :   List Notebooks

    onb :   Open Notebook
    nnb :   New Notebook

    nn  :   New Note

    q   :   Quit
    h   :   Help
"""

# Default Variables
notebooks = []
onb = 0     # currently open notebook
on = 0      # currently opened note


def initialize():
    'This fxn initializes app, loads all the notebooks'
    # load json data for notebooks
    global jd
    jd = open('data.json', 'r')
    for ntb in jd.readlines():
        jntb = json.loads(ntb)
        append_ntb = nb.notebook(jntb['title'])
        append_ntb.notelist = jntb['notelist']
        notebooks.append(append_ntb)


def finalize():
    'This fxn closes the apps, dumps the json'
    jd = open('data.json', 'w')

    for ntb in notebooks:
        jd.writeline(json.dumps(ntb, default=jdefault)+'\n')


def opennb(title):
    con = True  # temproray condition to check if notebook exists

    for ntb in notebooks:
        if ntb.title == title:
            print('Opened Notebook :', ntb.title)
            global onb
            onb = ntb
            con = False
            break
    if con:
        print('Notebook not found, use nnb to create one')


def parse(arg):
    'Parser for app console, returns note and notebook objects'
    arguments = arg.split()  # Split arguments
    global on, onb

    if len(arguments):

        if arguments[0] == 'onb' or arguments[0] == 'opennotebook':
            if len(arguments) == 2:
                onb = opennb(arguments[1])

        if arguments[0] == 'lnb' or arguments[0] == 'listnotebook':
            print('The following notebook are present :')
            for ntb in notebooks:
                print(' *', ntb.title)

        if arguments[0] == 'nnb' or arguments[0] == 'newnotebook':
            if len(arguments) == 1:
                onb = nb.notebook()
                notebooks.append(onb)

            else:
                onb = nb.notebook(arguments[1])
                notebooks.appned(onb)

        if arguments[0] == 'nn' or arguments[0] == 'newnote':
            if onb:
                if len(arguments) == 1:
                    on = nb.note()

                elif len(arguments) == 2:
                    on = nb.note(title=arguments[1])

                elif len(arguments) == 3:
                    on = nb.note(title=arguments[1], node=onb.title)

            else:
                print('No Notebook Opened open a notebook first')

        if arguments[0] == 'h' or arguments[0] == 'help':
            print(manual)
        if arguments[0] == 'q' or arguments[0] == 'quit':
            quit()


if __name__ == "__main__":

    while True:
        parse(input('#>'))

    finalize()
