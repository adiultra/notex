# Notex :pencil:

A python based command line note editor :fire: Work in Progress :fire:

---

# Reference

## NAME

__notebook__

### CLASSES
_builtins.object_

- note
- notebook

#### class note(builtins.object)

Note class to simulate a note

Methods defined here:

- __init__(self, title='', tags=[], content='')

- addtag(self, tag)
    Add a tag to note

- display(self)
    Display the note, This uses `pager` since the notes may be long

- edit

- finish

- rewrite


#### class notebook(builtins.object)

Notebook class, a container for notes

Methods defined here:

- __init__(self, title='')

- display(self)
    Display the title of notes of notebook

- newnote(self)
