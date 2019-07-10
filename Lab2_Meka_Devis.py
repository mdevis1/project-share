# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:11:41 2019

@author: devis
"""
import csv
file=open('baby-names.csv')
reader=csv.reader(file)
a_line_after_header = next(reader)
class Profile:
    year=0
    name=""
    percent=0
    sex=""
babylist=[]   
for row in reader:
    baby=Profile()
    baby.name=row[1]
    baby.percent=float(row[2])
    baby.sex=row[3]
    baby.year=int(row[0])
    babylist.append(baby)
#feature1
babyname=list(map(lambda x: x.name, babylist))
babyperc=list(map(lambda x: x.percent,babylist))
babyyear=list(map(lambda x: x.year,babylist))
print("The most popular baby",babyname[babyperc.index(max(babyperc))],"with a percentage " , 100* max(babyperc),"% in the year",babyyear[babyperc.index(max(babyperc))])
#feature2
babygender=input("Input your gender")
babystyle=input("Input your style")
if babystyle=="modern":
    filter1 = list(filter(lambda x: x.year >= 1990, babylist))
    filter2=list(filter(lambda x: x.sex==babygender, filter1))
    babymaxperc=list(map(lambda x: x.percent,filter2))
    reccomendlist=list(map(lambda x: x.name,filter2))
    print("We reccomend the name",reccomendlist[babymaxperc.index(max(babymaxperc))],"with a percentage " , 100* max(babymaxperc))
elif babystyle=="classic":
    filter1 = list(filter(lambda x: x.year < 1990, babylist))
    filter2=list(filter(lambda x: x.sex==babygender, filter1))
    babymaxperc=list(map(lambda x: x.percent,filter2))
    reccomendlist=list(map(lambda x: x.name,filter2))
    print("We reccomend the name",reccomendlist[babymaxperc.index(max(babymaxperc))],"with a percentage " , 100* max(babymaxperc))
else:
    filter2=list(filter(lambda x: x.sex==babygender, babylist))
    babymaxperc=list(map(lambda x: x.percent,filter2))
    reccomendlist=list(map(lambda x: x.name,filter2))
    print("We reccomend the name",reccomendlist[babymaxperc.index(max(babymaxperc))],"with a percentage " , 100* max(babymaxperc))

#feature3
yeardictionary={}
nameulike=input("Enter a name you like")
#return the year when the name was popular
filter4 = list(filter(lambda x: x.name==nameulike, babylist))
year=filter4[0].year
gender=filter4[0].sex
print("This name was popular in ",year)
print(gender)
filter5=list(filter(lambda x: x.year==year, babylist))
filter6=list(filter(lambda x: x.sex==gender, babylist))
if filter6[0].name==nameulike:
    print("We suggest the name",filter6[1].name)
else:
    print("We suggest the name",filter6[0].name)
#feature4
pts = []
minc=1880
maxc=2008
nametoplot=input("Enter a name you like")
filter6=list(filter(lambda x: x.name==nametoplot, babylist))
filter7=list(filter(lambda x: x.year > 1880, filter6))
filter8=list(filter(lambda x: x.year < 2008, filter7))
for i in range(len(filter8)):
    pts.append(filter8[i].percent)

import matplotlib.pyplot as plt
plt.plot(pts)
plt.show()





