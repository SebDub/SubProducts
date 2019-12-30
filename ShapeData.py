import pandas as pd
from zipfile import ZipFile

zip_file_prior = ZipFile('data/order_products__prior.csv.zip')
PriorOrders = pd.read_csv(zip_file_prior.open('order_products__prior.csv'))

zip_file_train = ZipFile('data/order_products__train.csv.zip')
TrainOrders = pd.read_csv(zip_file_train.open('order_products__train.csv'))

print(PriorOrders.shape)
print(TrainOrders.shape)
print(TrainOrders.head())