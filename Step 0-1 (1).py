import pandas as pd
import geopandas
import matplotlib.pyplot as plt

# Read file
df = pd.read_csv("Traffic_Violations.csv")

# Geo plot

g = df.groupby("SubAgency").count()
#
x = g.index.tolist()
print(x)
x1 =[]
for i in range(len(x)):
    b = "dist" + str((i+1))
    x1.append(b)
y = g["Description"].tolist()
#
plt.plot(x1, y)
plt.xlabel("District")
plt.ylabel("Traffic Violations")
plt.title("Violations per district")
plt.yticks([75,100,125,150,175,200,225,250], ["0","50K","100K","150K","200K","250K","300K","350K"])
plt.show()
