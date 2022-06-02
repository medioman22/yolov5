from helpers import *


if __name__ == "__main__":
    # download coco

    download_data()
    download_labels()

    # relabel
    relabel_coco(dir = '/workspace/datasets/coco/labels', remove_images_without_labels = True, subset = None)

