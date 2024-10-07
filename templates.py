import os
from pathlib import Path

list_of_files= [
    "experimentations/experimentations.ipynb",
    ".gitignore",
    "init_setup.sh",
    "requirements.txt",
    "app.py"
    
]

for filepaths in list_of_files:
    filepaths = Path(filepaths)
    filedir, filename = os.path.split(filepaths)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print(f"Creating a folder: {filedir} for the file: {filename}")
    if (not os.path.exists(filepaths)) or (os.path.getsize(filepaths) == 0):
         with open(filepaths, "w") as f:
             pass
    else:
        print(f"{filepaths} already exists!")