import os
import edit


class note:
    def __init__(self):
        self.title = input('Enter the note title :')
        self.tags = input('Enter Tags :').split(', ')
        self.content = edit.editor(
            box=False,
            title=self.title,
            win_location=(2, 2)
        )

        os.system('touch notebook/'+self.title+'.txt')
        self.file = open('notebook/'+self.title+'.txt', 'r+')
        self.rewrite()

    def display(self):
        os.system('pager notebook/'+self.title+'.txt')

    def edit(self):
        self.content = edit.editor(
            box=False,
            title=self.title,
            inittext=self.content,
            win_location=(2, 2)
        )

    def addtag(self, tag):
        self.tags.append(tag)

    def rewrite(self):
        towrite = 'Title : '+self.title+'\n\n'
        towrite += repr(self.tags)+'\n\n'
        towrite += self.content
        self.file.write(towrite)

    def finish(self):
        self.file.close()


class notebook:
    def __init__(self, title):
        self.title = title
        self.notelist = []

    def display(self):
        print('\nThe following notes are in', self.title)
        for note in self.notelist:
            print('*', note.title)

    def newnote(self):
        self.notelist.append(note())
        self.notelist[-1].finish()

# nb = notebook('Mongoose')
# nb.newnote()
# nb.display()

n = note()

# edit.editor(box=False, inittext="Hi", win_location=(5, 5))
