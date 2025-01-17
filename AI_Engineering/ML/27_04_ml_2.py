# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1W_-rPjGLWfZzVfL5vfPZgV5HV81CdmaX
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# X ve y değerlerini ayrı ayrı dönüştürerek verileri import etmek
X,y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train,y_test =train_test_split(X,y,test_size=0.20,
                                                  random_state=0)

clf = LogisticRegression(random_state=0)
clf.fit(X_train,y_train)


# Model Tahminlerinin yapılması ve doğruluğun hesaplanması

y_pred= clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("LogReg Accuracy Score (in%):",acc*100)

#Karar Sınırı Çizme
x_values=np.linspace(np.min(X[:,0]),np.max(X[:,0]),100)
y_values = -(clf.coef_[0][0]* x_values + clf.intercept_[0]) / clf.coef_[0][1]

# Görselleştirme

plt.figure(figsize=(10,6))
plt.scatter(X[:,0],X[:,1],c=y,cmap='bwr', edgecolors='k',label="Veri Noktaları")
plt.plot(x_values, y_values, color='green',linestyle='--',label='Karar Sınırı')
plt.xlabel("Ozellik 1")
plt.ylabel("Ozellik 2")
plt.title("LogReg Meme Kanseri Gors")
plt.legend()
plt.grid(True)
plt.colorbar(label="Sınıf")
plt.show()

