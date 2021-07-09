import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier

filelocation = 'insurance.csv'
df = pd.read_csv(filelocation)
df = df.drop(columns='ResponseNumeric')
df = df.drop(columns='Effective To Date')
df = df.drop(columns='State Code')
dfx = df.pop('State')
y = df.pop('Response')
x = pd.get_dummies(df)

x.to_csv('cleaned.csv', index=False)



# 70% training and 30% test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=110)

#clf = KNeighborsClassifier(n_neighbors=3)
clf = GaussianNB()
#clf = LogisticRegression(random_state=0, max_iter=1000)
#clf = svm.SVC(kernel='linear')
#clf = RandomForestClassifier()
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

#cm = metrics.confusion_matrix(y_test, y_pred)
#sns.heatmap(cm, square=True, annot=True, fmt='d', cbar=False,
            #xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
#plt.xlabel('Actual')
#plt.ylabel('Predicted')

names = np.unique(y_pred)

mat = metrics.confusion_matrix(y_pred, y_test)
names = np.unique(y_pred)
sns.heatmap(mat, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
plt.xlabel('Actual')
plt.ylabel('Predicted')
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

