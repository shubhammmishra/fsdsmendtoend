import os
path = 'notebook/first/second/research.ipynb'
path2 = 'notebook/first/second/research2.ipynb'
print(path)
dir, file = os.path.split(path)
print(dir)
print(file)
os.makedirs(dir, exist_ok=True)
with open(path, "w") as f:
    pass
with open(path2, "w") as t:
    pass
