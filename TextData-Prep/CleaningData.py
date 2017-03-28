# Convert all to lowercase
dataset['title'] = dataset['title'].map(lambda x: str(x).lower() )
dataset['description'] = dataset['description'].map(lambda x: str(x).lower() )
dataset['productBrand'] = dataset['productBrand'].map(lambda x: str(x).lower() )
dataset['keySpecsStr'] = dataset['keySpecsStr'].map(lambda x: str(x).lower() )
dataset['detailedSpecsStr'] = dataset['detailedSpecsStr'].map(lambda x: str(x).lower() )
dataset['sellerName'] = dataset['sellerName'].map(lambda x: str(x).lower() )