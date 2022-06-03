import download_relabel_coco
import add_egohands_to_coco

if __name__ == "__main__":

    download_relabel_coco.download_and_process()
    add_egohands_to_coco.download_and_process()