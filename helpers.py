import os
import shutil
import subprocess

from utils.general import download, Path
import yaml
import glob

import pandas as pd

def download_data(dir = None):
    # Download labels
      # segment or box labels
    if dir==None:
        dir = Path('/workspace/datasets/coco/')  # dataset root dir

    ##
    # Download data
    urls = ['http://images.cocodataset.org/zips/train2017.zip',  # 19G, 118k images
    ]
    download(urls, dir=dir / 'images', threads=3)

    ##
    # Download data
    urls = ['http://images.cocodataset.org/zips/val2017.zip',  # 1G, 5k images
    ]
    download(urls, dir=dir / 'images', threads=3)

def download_labels(dir = None, segments = False):
    ##
    if dir==None:
        dir = Path('/workspace/datasets/coco/')  # dataset root dir
    # Download labels
    url = 'https://github.com/ultralytics/yolov5/releases/download/v1.0/'
    urls = [url + ('coco2017labels-segments.zip' if segments else 'coco2017labels.zip')]  # labels
    download(urls, dir=dir.parent)

    import os

# relabel
def relabel_coco(dir = None, remove_images_without_labels = False, subset = None):

    if dir == None:
        dir = '/workspace/datasets/coco/labels'

    original_classes = {0: u'__background__',
    1: u'person',
    2: u'bicycle',
    3: u'car',
    4: u'motorcycle',
    5: u'airplane',
    6: u'bus',
    7: u'train',
    8: u'truck',
    9: u'boat',
    10: u'traffic light',
    11: u'fire hydrant',
    12: u'stop sign',
    13: u'parking meter',
    14: u'bench',
    15: u'bird',
    16: u'cat',
    17: u'dog',
    18: u'horse',
    19: u'sheep',
    20: u'cow',
    21: u'elephant',
    22: u'bear',
    23: u'zebra',
    24: u'giraffe',
    25: u'backpack',
    26: u'umbrella',
    27: u'handbag',
    28: u'tie',
    29: u'suitcase',
    30: u'frisbee',
    31: u'skis',
    32: u'snowboard',
    33: u'sports ball',
    34: u'kite',
    35: u'baseball bat',
    36: u'baseball glove',
    37: u'skateboard',
    38: u'surfboard',
    39: u'tennis racket',
    40: u'bottle',
    41: u'wine glass',
    42: u'cup',
    43: u'fork',
    44: u'knife',
    45: u'spoon',
    46: u'bowl',
    47: u'banana',
    48: u'apple',
    49: u'sandwich',
    50: u'orange',
    51: u'broccoli',
    52: u'carrot',
    53: u'hot dog',
    54: u'pizza',
    55: u'donut',
    56: u'cake',
    57: u'chair',
    58: u'couch',
    59: u'potted plant',
    60: u'bed',
    61: u'dining table',
    62: u'toilet',
    63: u'tv',
    64: u'laptop',
    65: u'mouse',
    66: u'remote',
    67: u'keyboard',
    68: u'cell phone',
    69: u'microwave',
    70: u'oven',
    71: u'toaster',
    72: u'sink',
    73: u'refrigerator',
    74: u'book',
    75: u'clock',
    76: u'vase',
    77: u'scissors',
    78: u'teddy bear',
    79: u'hair drier',
    80: u'toothbrush'}


    original_classes_inv = {original_classes[x]:x for x in original_classes.keys()}
    classes_keep = ['cup', 'laptop', 'mouse', 'keyboard', 'cell phone', 'book']
    classes_keep_nums = [original_classes_inv[x] for x in classes_keep]
    classes_keep_nums = [x-1 for x in classes_keep_nums]
    classes_keep_nums

    remap = {classes_keep_nums[idx]:idx for idx in range(len(classes_keep_nums))}

    remap

    filenames = glob.glob(dir+'/*/*.txt')
    filenames.sort()
    # print(filenames)

    
    if subset==None:
      subset = len(filenames)

    def remove_img_label(filename):
      
        # print(f'deleting image + label for {filename}')
        os.remove(filename.replace('labels', 'images').replace('txt', 'jpg'))
        os.remove(filename)
      

    for idx, filename in enumerate(filenames[:subset]):
        try:
            labels = pd.read_csv(filename, delimiter=' ', header=None)
            lab_corr = labels.loc[labels[0].isin(classes_keep_nums)]
            lab_corr = lab_corr.replace({0: remap})
            if remove_images_without_labels and len(lab_corr)==0:
              remove_img_label(filename)
            else:
              lab_corr.to_csv(filename, index = False, header = False, sep = ' ')
              # print(f"corrected {filename}")
        except:
            # print(f"no labels in {filename}")
            
            if remove_images_without_labels:
              remove_img_label(filename)
            pass
        if not idx%100:
            print(f"done {idx} of {subset} ({idx/subset*100:.2f}%)")

import os

# relabel
def relabel_hands(dir = None, remove_images_without_labels = False, subset = None, offset = 0):

    if dir == None:
        dir = '/workspace/datasets/coco/labels'

    original_classes = {0: u'__background__',
    1: u'myleft',
    2: u'myright',
    3: u'yourleft',
    4: u'yourright'}


    original_classes_inv = {original_classes[x]:x for x in original_classes.keys()}
    classes_keep = ['myleft', 'myright', 'yourleft', 'yourright']
    classes_keep_nums = [original_classes_inv[x] for x in classes_keep]
    classes_keep_nums = [x-1 for x in classes_keep_nums]
    classes_keep_nums

    remap = {classes_keep_nums[idx]:idx+offset for idx in range(len(classes_keep_nums))}

    remap

    filenames = glob.glob(dir+'/*/*.txt')
    filenames.sort()
    # print(filenames)

    
    if subset==None:
      subset = len(filenames)

    def remove_img_label(filename):
      
        # print(f'deleting image + label for {filename}')
        os.remove(filename.replace('labels', 'images').replace('txt', 'jpg'))
        os.remove(filename)
      

    for idx, filename in enumerate(filenames[:subset]):
        try:
            labels = pd.read_csv(filename, delimiter=' ', header=None)
            lab_corr = labels.loc[labels[0].isin(classes_keep_nums)]
            lab_corr = lab_corr.replace({0: remap})
            if remove_images_without_labels and len(lab_corr)==0:
              remove_img_label(filename)
            else:
              lab_corr.to_csv(filename, index = False, header = False, sep = ' ')
              # print(f"corrected {filename}")
        except:
            # print(f"no labels in {filename}")
            
            if remove_images_without_labels:
              remove_img_label(filename)
            pass
        if not idx%100:
            print(f"done {idx} of {subset} ({idx/subset*100:.2f}%)")

