# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:38:52 2019

@author: devis
"""

import pandas as pd
import geopandas
import matplotlib.pyplot as plt

# Read file
df = pd.read_csv("Traffic_Violations.csv")
df['Time Of Stop'] = pd.to_datetime(df['Time Of Stop'])
df=df[df['Alcohol']=='Yes']
#df=df[df['Belts']=='Yes']
df = df.groupby(pd.Grouper(key='Time Of Stop', freq='3H'))
plt.title('Alcohol & Seatbelt Violations')
#df["Belts"].count().plot()
df["Alcohol"].count().plot()
plt.show()