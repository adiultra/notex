import notebook as nb
import json

data = open("data.json", 'r+')

notebook = nb.notebook()

notes = json.load(data)
