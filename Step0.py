# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# Read file and take only the first 10000 rows with applicable columns.
# Apparently the graphs look different and better on the larger(original) file. 
#But for efficiency let's stick with these.:-)
data = pd.read_csv("Traffic_Violations.csv", nrows = 10000)
df = pd.DataFrame(data, columns = ["Date Of Stop", "Time Of Stop", "Description", "SubAgency", "VehicleType", "Latitude", "Longitude", "Accident", "Belts", "State", "Geolocation"]) 
#After initial analysis we realized that we have  agencies with the names S15 and W15
# but they do not have any violations registered and we romoved those rows.
df = df[(df.SubAgency != "S15") & (df.SubAgency !="W15")]
print(str(len(df)) + " records were read from this file")

print("Feature #1")
print("="*70)
# Ploting the distribution of vilation per district by SubAgency chart
df1 = df.groupby("SubAgency").count()
x = df1.index.tolist()
#check what the list of districts look like
print("We hava data for the following districts:")
for i in x:
    print(i)

#shortening the names in the list for better visualization &populating x and y axis
x1 =[]
for i in range(len(x)):
    b = "dist" + str((i+1))
    x1.append(b)
y = df1["Description"].tolist()

plt.plot(x1, y)
plt.xlabel("District")
plt.ylabel("Traffic Violations")
plt.title("Violations per district")
#renaming the yticks for better visualization. It makes sense only for the 
#original(larger) file
plt.yticks([0,50000, 100000,150000,200000,250000,300000,350000],["0","100K","150K","200K","250K","300K","350K"])
plt.show()
#the graph visualization looks much better(and diferrent when applied to the whoule dataset)
#sorting the # of violations per dist and diplaying the max
df1 = df1.sort_values(by = ["Time Of Stop"], ascending = False)
df1 = df1["Time Of Stop"]
print("Top 3 agencies with most violations")
print(df1.head(3))

print("\nFeature #2")
print("="*70)
# Filtering only the violations resulting in an accident.
df2 = df[df['Accident'] == "Yes"]
df2['Time Of Stop'] = pd.to_datetime(df2['Time Of Stop'])
df2 = df2.groupby(pd.Grouper(key='Time Of Stop', freq='1H'))
#ploting the distribution of violations resuting in an accident relative to time of occurance
df2['Accident'].count().plot()
plt.ylabel("Number of Accidents")
plt.title("Accidents Distribution in 24 hours")
plt.show()
