def findatag(file):
  import pandas as pd
  Names = ["Name"]
  df = pd.read_csv("tags.csv", usecols=Names)
