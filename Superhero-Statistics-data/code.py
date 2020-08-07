# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)
data.head()
data.isnull().sum()
# Code starts here
data['Gender'].value_counts()
data['Gender'] = data['Gender'].replace('-', 'Agender')
x = data['Gender'].value_counts(ascending=False)
fig = plt.figure(figsize=(5, 5))
x.plot(kind='bar')
plt.title('Distribution of Gender', fontsize=16, color='blue')
plt.xlabel('Gender')
plt.ylabel('Numbers')
plt.show()

y = data['Alignment'].value_counts(ascending=False)
fig = plt.figure(figsize=(5, 5))
y.plot(kind='bar')
plt.title('Distribution of Alignment', fontsize=16, color='blue')
plt.xlabel('Alignment')
plt.ylabel('Numbers')
plt.show()

newdf = data[['Strength', 'Intelligence']].copy()

covariance = newdf.cov()
covariance = covariance['Intelligence'].iloc[0]
std_strength = newdf['Strength'].std()
std_intelligence = newdf['Intelligence'].std()

pearson = covariance / (std_strength*std_intelligence)
print(pearson)

q1 = data.Total.quantile(q=0.99)
z = data[data['Total']>q1]
super_best_names = list(z['Name'])
print(super_best_names)



