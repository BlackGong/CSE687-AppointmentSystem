import os
COMPUTER_NAME = os.environ['COMPUTERNAME'] #do not need to change
print("Computer: ", COMPUTER_NAME)

WORKER_POOL_SIZE = 8

TARGET_VOXEL_MM = 1.00
MEAN_PIXEL_VALUE_NODULE = 41
LUNA_SUBSET_START_INDEX = 0
SEGMENTER_IMG_SIZE = 320

BASE_DIR_SSD = "E:/687proj/ndsb3_c/" # create the folder name ndsb3 for saving the corresponding results
BASE_DIR = "E:/687proj/ndsb3/" # create the folder name ndsb3 for placing the input data here
EXTRA_DATA_DIR = "resources/" # place here extra data
NDSB3_RAW_SRC_DIR = BASE_DIR + "ndsb_raw/stage1/" # place here the kaggle data which will further
LUNA16_RAW_SRC_DIR = BASE_DIR + "luna_raw/" # place here the LUNA16 database

NDSB3_EXTRACTED_IMAGE_DIR = BASE_DIR_SSD + "ndsb3_extracted_images/"
LUNA16_EXTRACTED_IMAGE_DIR = BASE_DIR_SSD + "luna16_extracted_images/" # create a "_labels"
NDSB3_NODULE_DETECTION_DIR = BASE_DIR_SSD + "ndsb3_nodule_predictions/"
LUNA_NODULE_DETECTION_DIR = BASE_DIR_SSD + "luna16_nodule_predictions/"
