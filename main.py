from script import download ,data_cleaned,remove_attributes
url='https://raw.githubusercontent.com/12alain/python/master/data/billets.csv'
download(url)
data_cleaned()
remove_attributes()