# -*- coding: utf-8 -*-
"""Iris Flower Classification

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KD1ZyPe3YQniz73KUeUPCesX5xuloY-3
"""

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score,f1_score,recall_score,precision_score

data=pd.read_csv('/content/Iris.csv')

data.head()

data.shape

data.isnull()

data.describe()

data.info()

data.size

data.isnull().sum()

data.drop(columns='Id',axis=0,inplace=True)

data_split=data.Species.str.split('-',n=-1,expand=True)
data_split.drop(columns=0,axis=1,inplace=True)

data_split

data_full=data.join(data_split)
data_full

data.dtypes

data_full.rename({1:'Spacies1'},axis=1,inplace=True)
data_full

data_full.drop(columns='Species',axis=1,inplace=True)
data_full

data_full.shape

data_full.isnull()

data_full.isnull().sum()

data_full.corr()

data_full.Spacies1.value_counts()

data.Species.value_counts()

sns.FacetGrid(data, hue="Species", height=7).map(plt.scatter, "SepalLengthCm", "PetalLengthCm").add_legend()

x=data[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']].values
y=data[['Species']].values

model=LogisticRegression()
model.fit(x,y)

model.score(x,y).round(4)

Actual=y
predicted=model.predict(x)

from sklearn import metrics
print(metrics.classification_report(Actual,predicted))

print(metrics.confusion_matrix(Actual,predicted))

predicted=model.predict([[4.6,3.2,1.4,0.2]])
predicted

predicted=model.predict([[7.7,2.8,6.7,2]])
predicted

predicted=model.predict([[1.9,4.2,2.7,1],[4.1,6,2,3],[1.0,2.5,6,0.4]])
predicted