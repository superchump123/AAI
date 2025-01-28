import shutil
import os

def move_data():
    for file in os.listdir(os.getcwd()):
        print(file)
        if file.endswith('.json'):
            shutil.move(file, 'data/cocktaildb/' + file)