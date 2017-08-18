from os import listdir
from os.path import isfile
import os

#check whether file extension match argument
def isfiletype(filename,ext):
    return(filename[len(filename)-len(ext):]==ext)

#format folder to make sure it ends with '/'
def format_path(path):
    if(path[len(path)-1]=='/'):
        return path
    else:
        return path+'/'

def get_current_folder():
    return os.getcwd()[os.getcwd().rindex('\\')+1:]

def path_exists(path):
    return os.path.exists(path)

if __name__ == "__main__":
    filename = 'longtestmaggle.csv'
    ext = '.csv'
    print(isfiletype(filename,ext))
    path = 'toto_path/toto'
    print(format_path(path))
    print('get_curent_folder: ' + get_current_folder())
