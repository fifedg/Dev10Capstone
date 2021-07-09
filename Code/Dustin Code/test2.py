import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns; sns.set()

filelocation = 'insurance2.csv'
df = pd.read_csv(filelocation)

plt.figure(figsize=(20, 10))
sns.heatmap(df.corr(), annot=True, fmt=".2f")
