import os, os.path
import uuid

DOWNLOAD_PATH = "images/"
CHROMEDRIVER_PATH = "Put Chromedriver path here"

def number_of_files_inside_the_folder():

    return len([name for name in os.listdir(DOWNLOAD_PATH) if os.path.isfile(os.path.join(DOWNLOAD_PATH, name))]) + 1


def directory_exists():
    if not os.path.exists(DOWNLOAD_PATH):
        os.mkdir(DOWNLOAD_PATH)

def file_exists(filename):
    try:
        with open(filename, 'r') as f:
            return True
    except IOError: 
        return False   
    

def get_random_hash():
    
    hash = uuid.uuid4().hex + uuid.uuid4().hex
    
    while file_exists(DOWNLOAD_PATH + hash + ".jpg"):
        
        hash = uuid.uuid4().hex + uuid.uuid4().hex
        
    return hash


def rename_file():    
        
    for filename in os.listdir(DOWNLOAD_PATH):

        hash = get_random_hash()

        while file_exists(DOWNLOAD_PATH + hash + ".jpg"):
            
            hash = get_random_hash()
        
        old_name = DOWNLOAD_PATH + filename
        new_name = DOWNLOAD_PATH + hash + '.jpg'
        os.rename(old_name, new_name)