import os
import edit

'''
Terminologies:

node :
    the container or root, in this case notebook is node for a note
    bare :
        A note with no notebook. A spare note.
'''


class note:
    'Note class to simulate a note'

    def __init__(
        self,
        title='',
        tags=[],
        content='',
        node='bare'
    ):
        if len(title):
            self.title = title
        else:
            self.title = input('Enter Note title : ')

        if len(tags):
            self.tags = tags
        else:
            self.tags = input('Enter tags : ').split(', ')

        if len(content) == 0:
            self.content = edit.editor(
                box=False,
                title=self.title,
                win_location=(2, 2)
            )

        else:
            self.content = content

        self.node = node

        self.file = open('notebook/'+self.title+'.txt', 'w')
        self.rewrite()

    def display(self):
        'Display the note, This uses `pager` since the notes may be long'
        os.system('pager notebook/'+self.title+'.txt')

    def edit(self):
        'Edit the note content'
        self.content = edit.editor(
            box=False,
            title=self.title,
            inittext=self.content,
            win_location=(2, 2)
        )

    def addtag(self, tag):
        'Add a tag to note'
        self.tags.append(tag)

    def rewrite(self):
        'Rewrite the note to the file, works as a save function'
        towrite = 'Title : '+self.title+'\n\n'
        towrite += repr(self.tags)+'\n\n'
        towrite += self.content

        self.file.write(towrite)

    def finish(self):
        'Close the file'
        self.file.close()


class notebook:
    'Notebook class, a container for notes'

    def __init__(self, title=''):
        if len(title):
            self.title = title
        else:
            self.title = input('Enter NoteBook title : ')
        self.notelist = []

    def display(self):
        'Display the title of notes of notebook'
        print('\nThe following notes are in', self.title)

        for note in self.notelist:
            print('*', note.title)

    def newnote(self):
        self.notelist.append(note(node=self.title))
        self.notelist[-1].finish()


def parser(arg):
    'Parser for app console, returns note and notebook objects'
    arguments = arg.split()  # Split arguments

    if len(arguments):
        if arguments[0] == 'nnb' or arguments[0] == 'newnotebook':

            if len(arguments) == 1:
                return notebook()

            else:
                return notebook(arguments[1])

        if arguments[0] == 'nn' or arguments[0] == 'newnote':

            if len(arguments) == 1:
                return note()

            else:
                return note(arguments[1])

        if arguments[0] == 'q' or arguments[0] == 'quit':
            quit()

# nb = notebook('Mongoose')
# nb.newnote()
# nb.display()

# n = note() $>

# edit.editor(box=False, inittext="Hi", win_location=(5, 5))
