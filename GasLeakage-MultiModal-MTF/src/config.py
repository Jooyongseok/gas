import torch

DATA_DIR_SENSOR   = '/project/ahnailab/data/gas/Gas Sensor HM'
DATA_DIR_THERMAL  = '/project/ahnailab/data/gas/Thermal Camera Images'
DATA_DIR_SENSOR_CSV = '/project/ahnailab/data/gas/Gas_Sensors_Measurements.csv'

BATCH_SIZE  = 8
EPOCHS      = 3
NUM_CLASSES = 4
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
LABEL_MAP = {'Mixture': 0, 'NoGas': 1, 'Perfume': 2, 'Smoke': 3}

ORIGINAL_DATA  = '/project/ahnailab/data/gas/Gas_Sensors_Measurements.csv'
TRAIN_CSV_PATH = '/project/ahnailab/data/gas/TRAIN_DATA.csv'
TEST_CSV_PATH  = '/project/ahnailab/data/gas/TEST_DATA.csv'