# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 21:10:58 2019

@author: devis

"""


import csv
file=open('2015_PUDB_EXPORT_123115 (1).csv')
reader=csv.reader(file)
reader1=next(reader)
class Loan:
    income=0
    age=0
    creditsco=0
    amount=0
    rate=0
 
        
def strictly_increasing(L):
    return all(x<y for x, y in zip(L, L[1:]))
def strictly_decreasing(L):
    return all(x>y for x, y in zip(L, L[1:]))

i=0  
loanlist=[] 
for row in reader:
    loan=Loan()
    if int(row[4])==9:
        i+=1
    else:
        loan.creditsco=int(row[4])
        loan.income=int(row[0])
        loan.age=int(row[1])
        loan.rate=float(row[2])
        loan.amount=int(row[3])
        loanlist.append(loan)
print("There are",i,"missing record")
print("Analyzing",len(loanlist))
#feature2
y=[]
x=[]
for i in range(1,6):
    avglist=list(filter(lambda x: x.creditsco==i, loanlist))
    avgloan=list(map(lambda x: x.amount,avglist))
    avg=sum(avgloan)/len(avgloan)
    y.append(avg)
    x.append(int(i))
import matplotlib.pyplot as plt
#plt.plot(x,y)
#plt.show()
xx=[]
yy=[]
for i in range(1,6):
    avglist=list(filter(lambda x: x.creditsco==i, loanlist))
    avgint=list(map(lambda x: x.rate,avglist))
    avg=sum(avgint)/len(avgint)
    yy.append(avg)
    xx.append(i)
plt.plot(xx,yy)
plt.show()
print(xx)
print(yy)
if strictly_increasing(y):
    print("wow it is healthy")
if strictly_decreasing(yy):
    print("wow it is healthy")

        
