# 1) create a data folder
# 2) batch download the data from kaggle there
# 3) unzip them there


def DownloadData(dirName: str = 'data') -> None:

    import os

    """Dowload the data from instacart on Kaggle

        Input dirname: str with the directory
        (existing or to be created)
        to store the data
    """

    fileName = f'{dirName}.zip'

    # Create directory
    try:
        os.mkdir(dirName)
        print(f'Directory {dirName} created')
    except FileExistsError:
        print(f'Directory {dirName} already exists')

    if(not os.path.exists(f'{dirName}/{fileName}')):
        os.system('kaggle competitions download -c \
            instacart-market-basket-analysis')
        os.rename('instacart-market-basket-analysis.zip',
                  f'{dirName}/{fileName}')


def UnzipData(dirName: str = 'data') -> None:

    import os
    import zipfile
    fileName = f'{dirName}.zip'
    # first extraction
    with zipfile.ZipFile(f'{dirName}/{fileName}', 'r') as zip_ref:
        zip_ref.extractall(f'{dirName}/')
    # removal of the file
    os.remove(f'{dirName}/{dirName}.zip')
    # unziping the csv.zip files
    files = [f for f in os.listdir(dirName) if f.endswith(".csv.zip")]

    for fi in files:
        # unziping
        with zipfile.ZipFile(f'{dirName}/{fi}') as zipfi:
            zipfi.extract(f'{fi[:-4]}', f'{dirName}')
        # removal
        os.remove(f'{dirName}/{fi}')
