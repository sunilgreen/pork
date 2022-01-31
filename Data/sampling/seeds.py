from curses import raw
import random
import pandas as pd

def getSample(df, col, value, seed, n):
    specificdf = df.loc[df[col] == value]
    datapoints = specificdf.index.tolist() 
    random.seed(seed)
    points = random.sample(datapoints, n)
    points.sort()
    return points

rawData = pd.read_excel("./TCSEarmarks.xlsx")
# print(rawData.columns.values)

#Ag-Rural Development-FDA
#print(getSample(rawData, "Bill", "Ag-Rural Development-FDA", 11610, 21))

#Commerce, Justice & Science
#print(getSample(rawData, "Bill", "Commerce, Justice & Science", 11610, 34))

#Defense
#print(getSample(rawData, "Bill", "Defense", 11610, 55))

#Energy & Water
print(getSample(rawData, "Bill", "Energy & Water", 11610, 62))

#Financial Services
#print(getSample(rawData, "Bill", "Financial Services", 11610, 4))

#Homeland Security 
#print(getSample(rawData, "Bill", "Homeland Security", 11610, 4))

#Interior
#print(getSample(rawData, "Bill", "Interior", 11610, 4))

#Labor-HHS-Education
#print(getSample(rawData, "Bill", "Labor-HHS-Education", 11610, 4))

#Legislative Branch
#print(getSample(rawData, "Bill", "Legislative Branch", 11610, 4))

#Military Construction
#print(getSample(rawData, "Bill", "Military Construction", 11610, 4))

#State-Foreign Ops
#print(getSample(rawData, "Bill", "State-Foreign Ops", 11610, 4))

#Transporation and Housing & Urban Development
#print(getSample(rawData, "Bill", "Transporation and Housing & Urban Development", 11610, 4))


#print(rawData.loc[rawData['Bill'] == "Ag-Rural Development-FDA"].index.tolist())








    
