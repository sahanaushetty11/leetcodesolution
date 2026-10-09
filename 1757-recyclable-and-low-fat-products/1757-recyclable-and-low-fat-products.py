import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    lowfatrecycle_filter=((products['low_fats']=='Y') & (products['recyclable']=='Y'))
    return products.loc[ lowfatrecycle_filter,['product_id']]
    