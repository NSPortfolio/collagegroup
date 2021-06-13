import pandas as pd

def searchtool(file):
    df = pd.read_csv(file, usecols = ['Name'])
    df = df.Name.to_list()
    for x in searchtool('https://raw.githubusercontent.com/Times4Everyone/collagegroup/main/tags.csv'):
      print(x)
    html = '<form><input list="tags" name="tags"><datalist>'
    for options in x:
        html += '<option value=' + str(options) + '>'
    html += ' </datalist><a href = "getstarted.html" class="button"> Search </a></center></form>'
    webpage = open("names.txt","w+")
    webpage.write(html)
    return(html)
