from helpers import *

import subprocess
import shutil

def move_all_in_folder(fol, target_fol):
    file_names = os.listdir(fol)
        
    for file_name in file_names:
        shutil.move(os.path.join(fol, file_name), target_fol)


if __name__ == "__main__":
    # download coco


    # hands dataset 

    subprocess.run('curl -L -q "https://public.roboflow.com/ds/L4HgyEQXXH?key=eZpjwNJLf1" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip', shell=True)
    

    os.mkdir('images')
    os.mkdir('images/test')
    os.mkdir('images/train')
    os.mkdir('images/valid')

    os.mkdir('labels')
    os.mkdir('labels/test')
    os.mkdir('labels/train')
    os.mkdir('labels/valid')

    move_all_in_folder('test/images', 'images/test')
    move_all_in_folder('train/images', 'images/train')
    move_all_in_folder('valid/images', 'images/valid')

    move_all_in_folder('test/labels', 'labels/test')
    move_all_in_folder('train/labels', 'labels/train')
    move_all_in_folder('valid/labels', 'labels/valid')

    shutil.rmtree('test')
    shutil.rmtree('train')
    shutil.rmtree('valid')


    ws_dir='/workspace'

    if not os.path.exists(ws_dir):
        os.mkdir(ws_dir)
    if not os.path.exists(ws_dir+'/datasets'):
        os.mkdir(ws_dir+'/datasets')

    os.mkdir(ws_dir + '/datasets/hand_detect')
    shutil.move('labels', ws_dir+'/datasets/hand_detect')
    shutil.move('images', ws_dir+'/datasets/hand_detect')