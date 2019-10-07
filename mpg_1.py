import pandas as pd
import seaborn as sns


df=sns.load_dataset('mpg')
serie1=df.name[df.origin=='europe'].str.split().str[0]
dict1={'volkswagen': 'Germany', 'peugeot': 'France', 'audi': 'Germany', 'saab': 'Sweeden', 'bmw': 'Germany', 'opel': 'Germany', 'fiat': 'Italy', 'volvo': 'Sweeden', 'renault': 'France', 'vw': 'Germany', 'mercedes-benz': 'Germany', 'mercedes': 'Germany', 'vokswagen': 'Germany', 'triumph': 'England'}
for i in serie1.index:
	serie1[i]=dict1[serie1[i]]

df.loc[serie1.index, 'origin']=serie1
print(df.origin)
df.to_csv('out.csv',index=False)
