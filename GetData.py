# 1) create a data folder
# 2) batch download the data from kaggle there
# 3) unzip them there

import os

# Create directory
dirName = 'data'

try:
    # Create target Directory
    os.mkdir(dirName)
    print(f'Directory {dirName} Created')
except FileExistsError:
    print(f'Directory {dirName} already exists')

fileName = 'instacart-market-basket-analysis.zip'
if(~os.path.exists(f'{dirName}/{fileName}')):
    os.system('kaggle competitions download -c \
        instacart-market-basket-analysis')
    os.rename(fileName, f'{dirName}/{fileName}')
