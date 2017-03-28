# Convert all to lowercase
dataset['title'] = dataset['title'].map(lambda x: str(x).lower() )


# Combine all features into one
dataset['allTextFeaures'] = dataset['title'] + ' '  + dataset['description']