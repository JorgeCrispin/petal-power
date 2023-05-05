import codecademylib3
import pandas as pd
import pandas as pd
df = pd.read_csv('inventory.csv')
inventory = df
#print(inventory.head(10))
staten_island = inventory.head(10)
print(staten_island)                     
product_request = staten_island['product_description']
print(product_request)
inventory['in_stock'] = inventory['quantity'] > 0
print(inventory['in_stock'])

inventory['total_value'] = inventory['quantity'] * inventory['price']
print(inventory)
combine_lambda = inventory.apply(lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description), axis = 1)
inventory['full_description'] = combine_lambda
print(inventory)           