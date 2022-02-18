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

def getPoints(seed, n, start, stop):

    point_list = []
    for i in range(start, stop):
        point_list.append(i)

    random.seed(seed)
    points = random.sample(point_list, n)
    print("######### Random Sample #########")
    print(points)
    print("######### End Random Sample #########")
    return points

'''
The samples below are used for the manual identification of data.
Once issues with data cleaning are resolved this will be automated.
Only used for an intitial run. Because of the under-represenation of
pork in the combined data (assuming 10% pork per CAGW), samples
are taken from each seperate part of the data.
'''
getPoints(100, 27, 0, 12816) #Getting negative samples
getPoints(100, 3, 12816, 13233) #Getting positive samples

#rawData = pd.read_excel("./TCSEarmarks.xlsx")
# print(rawData.columns.values)

#Ag-Rural Development-FDA
#print(getSample(rawData, "Bill", "Ag-Rural Development-FDA", 11610, 21))

#Commerce, Justice & Science
#print(getSample(rawData, "Bill", "Commerce, Justice & Science", 11610, 34))

#Defense
#print(getSample(rawData, "Bill", "Defense", 11610, 55))

#Energy & Water
#print(getSample(rawData, "Bill", "Energy & Water", 11610, 62))

#Financial Services
#print(getSample(rawData, "Bill", "Financial Services", 11610, 35))

#Homeland Security 
#print(getSample(rawData, "Bill", "Homeland Security", 11610, 4))

#Interior
#print(getSample(rawData, "Bill", "Interior", 11610, 20))

#Labor-HHS-Education
#print(getSample(rawData, "Bill", "Labor-HHS-Education", 11610, 60))

#Legislative Branch
#print(getSample(rawData, "Bill", "Legislative Branch", 11610, 2))

#Military Construction
#print(getSample(rawData, "Bill", "Military Construction", 11610, 80)

#State-Foreign Ops
#print(getSample(rawData, "Bill", "State-Foreign Ops", 11610, 12))

#Transporation and Housing & Urban Development
#print(getSample(rawData, "Bill", "Transporation and Housing & Urban Development", 11610, 61))


#print(rawData.loc[rawData['Bill'] == "Ag-Rural Development-FDA"].index.tolist())








    
