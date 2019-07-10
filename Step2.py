# -*- coding: utf-8 -*-
"""
Created on Sat May 18 10:27:34 2019

@author: devis
"""

"""
Created on Fri May 10 22:06:19 2019

@author: devis
"""

import pandas as pd
import geopandas
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

df = pd.read_csv("Traffic_Violations.csv")
g=df.loc[df['Alcohol'] == 'Yes']
#h=df.groupby('SubAgency').size()
h=g.groupby('SubAgency').size().reset_index(name='counts')
h.plot()
plt.xlabel("District")
plt.ylabel("# of Alcohol Violations")
plt.title("Alcohol Violations per District")
plt.xticks([0,1,2,3,4,5,6], ["dist1","dist2","dist3","dist4","dist5","dist6","dist7"])
plt.show()
print(h)
