import os
import edit


class note:
    'Note class to simulate a note'

    def __init__(
        self,
        title=input('Enter the note title :'),
        tags=input('Enter Tags :').split(', '),
        content=''
    ):
        self.title = title
        self.tags = tags

        if len(content) == 0:
            self.content = edit.editor(
                box=False,
                title=self.title,
                win_location=(2, 2)
            )

        else:
            self.content = content

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

    def __init__(self, title=input('Title for notebook : ')):
        self.title = title
        self.notelist = []

    def display(self):
        'Display the title of notes of notebook'

        print('\nThe following notes are in', self.title)

        for note in self.notelist:
            print('*', note.title)

    def newnote(self):
        self.notelist.append(note())
        self.notelist[-1].finish()


def parse(arg):
    'Parser for app console, returns note and notebook objects'
    args = arg.split()  # Split arguments

    if len(args):
        if args[0] == 'nnb' or args[0] == 'newnotebook':

            if len(args) == 1:
                return notebook()

            else:
                return notebook(args[1])

        if args[0] == 'nn' or args[0] == 'newnote':

            if len(args) == 1:
                return note()

            else:
                return note(args[1])

# nb = notebook('Mongoose')
# nb.newnote()
# nb.display()

# n = note() $>

# edit.editor(box=False, inittext="Hi", win_location=(5, 5))
