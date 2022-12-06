from django import forms
import pandas as pd


filename = "P:\\Test_Log.csv"
chunksize = 10 ** 6
for chunk in pd.read_csv(filename,delimiter=";",low_memory=True, index_col=False, dtype="unicode",chunksize=chunksize):
    df = pd.DataFrame(chunk)
columns = []

df.dropna(axis='columns',how='all', inplace = True)
df.fillna('0', inplace =True)
df = df.loc[:, ~(df == '0').all()]
df.drop(['Time[s]'], axis =1, inplace = True)
columns = list(df)

CHOICES = tuple([(content,content) for content in columns])

class OptionsForm(forms.Form):
    
    filters = forms.MultipleChoiceField( choices=CHOICES, label= '')