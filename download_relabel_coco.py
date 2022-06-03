from helpers import *

def download_and_process():
    download_data()
    download_labels()

    # relabel
    relabel_coco(dir = '/workspace/datasets/coco/labels', remove_images_without_labels = True, subset = None)

if __name__ == "__main__":
    # download coco

    download_and_process()