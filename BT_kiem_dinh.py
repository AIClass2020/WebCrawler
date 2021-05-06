# -*- coding: utf-8 -*-
"""
Created on Thu May  6 09:27:49 2021

@author: Trần Thị Diệu Hiền
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import math
import numpy as np
from scipy import stats



data = pd.read_csv("C:\\Users\\DUC-PC\\Downloads\\data.csv")
screen = data['Screen Size']
weight = data['Weight']
brightness = data["Brightness"]
def hist_plot(data):
    mu = np.mean(data)
    sigma = np.std(data)
    x = np.linspace(mu - 3*sigma, mu + 3*sigma)
    plt.plot(x, stats.norm.pdf(x, mu, sigma), color = 'red')
    plt.hist(data, density=True, color = 'pink', edgecolor = 'red')
    plt.title(data.name)
    plt.show()

    
def qq_plot(data):
    sm.qqplot(data, line ='45', color = 'cyan')
    plt.show()
    

def bartlett(a, b, c):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Kiểm định Bartlett:")
    stat, pvalue = stats.bartlett(a, b, c)
    print("Statistic =", stat, "\n",
          "p value =", pvalue)
    if pvalue > 0.05:
        print("Các features đồng nhất về phương sai")
    else:
        print("Các features không đồng nhất về phương sai")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
        

def levene(a, b, c):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Kiểm định Levene:")
    stat, pvalue = stats.levene(a, b, c)
    if pvalue > 0.05:
        print("Các features đồng nhất về phương sai")
    else:
        print("Các features không đồng nhất về phương sai")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
    
def Shapiro(data):
    print("Kiểm định Shapiro -", data.name)
    stat, pvalue = stats.shapiro(data)
    if pvalue > 0.05:
        print("Không thể bác bỏ giả thiết H0: Phân phối của dữ liệu là chuẩn")
    else:
        print("Dữ liệu không tuân theo luật phân phối chuẩn")
    print("------------------------------")
    

def Kolmogorov(data):
    print("Kiểm định Kolmogorov -", data.name)
    k, p = stats.kstest(rvs=data, cdf='norm', args=(np.mean(data), np.std(data)))
    if p > 0.05:
        print("Không thể bác bỏ giả thiết H0: Phân phối của dữ liệu là chuẩn")
    else:
        print("Dữ liệu không tuân theo luật phân phối chuẩn")
    print("------------------------------")
        

hist_plot(screen)
hist_plot(weight)
hist_plot(brightness)
qq_plot(screen)
qq_plot(weight)
qq_plot(brightness)
print(bartlett(screen, weight, brightness))
print(Shapiro(screen))
print(Shapiro(weight))
print(Shapiro(brightness))   
print(levene(screen, weight, brightness))
print(Kolmogorov(screen))
print(Kolmogorov(weight))
print(Kolmogorov(brightness))  

