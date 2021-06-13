import pandas as pd

def searchtool(file):
    df = pd.read_csv(file, usecols = ['Name'])
    df = df.Name.to_list()
    for x in searchtool('https://raw.githubusercontent.com/Times4Everyone/collagegroup/main/tags.csv'):
      print(x)
