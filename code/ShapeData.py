import pandas as pd
import numpy as np
from zipfile import ZipFile

zip_file_prior = ZipFile('data/order_products__prior.csv.zip')
PriorOrders = pd.read_csv(zip_file_prior.open('order_products__prior.csv'))

zip_file_train = ZipFile('data/order_products__train.csv.zip')
TrainOrders = pd.read_csv(zip_file_train.open('order_products__train.csv'))

print(PriorOrders.shape)
print(TrainOrders.shape)
print(TrainOrders.head())

OrdersMerged = PriorOrders.append(TrainOrders). \
    drop(['add_to_cart_order', 'reordered'],
         axis=1, inplace=True)


print(PriorOrders.shape[0]+TrainOrders.shape[0])
print(OrdersMerged.shape[0])

del PriorOrders
del TrainOrders

#OrdersMergedPivot = Order
