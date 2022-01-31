import numpy as np
import pandas as pd
import re
import csv
import openpyxl

def makeList(csv1):
    df = pd.read_csv(csv1, encoding = "ISO-8859-1", engine ='python')
    df = df.drop(df.iloc[:, 0:8], axis=1)
    df = df.drop(df.iloc[:, 2:], axis=1)

    locationList = []
    
    for i in range(0, len(df)):
        
        townstr = df.iloc[i, 0]
        #print(re.split(".(\s[city])", townstr))
        place = re.split('\scity|\stown',townstr)
        final_str = place[0] + ", " + str(df.iloc[i, 1])
        locationList.append(final_str)

    locationsDataFrame = pd.DataFrame(locationList)

    specificLocations = []
    for i in range(0, len(df)):
        
        townstr = df.iloc[i, 0]
        #print(re.split(".(\s[city])", townstr))
        place = re.split('\scity|\stown',townstr)
        final_str = place[0]
        specificLocations.append(final_str)

    specificDataFrame = pd.DataFrame(specificLocations)
    specificDataFrame = specificDataFrame.drop_duplicates()

    #allLocations = pd.concat([locationsDataFrame, specificDataFrame])
    #print(allLocations)

    # locationsDataFrame.to_excel("../Data/locations.xlsx", index=False, header=False)
    # specificDataFrame.to_excel("../Data/specificLocations.xlsx", index=False, header=False)
    # allLocations.to_excel("../Data/allLocations.xlsx", index=False, header=False)
    
    #allLocations.to_csv("../Data/allLocations.csv", index=False, header=False)
    specificDataFrame.to_csv("../Data/specificLocations.csv", index=False, header=False)

def makeStates():
    df = pd.read_csv("../Data/rawStates.csv")
    states = df["State"]
    abbreviations = df["Abbreviation"]

    states.to_csv("../Data/states.csv", index=False, header=False)
    abbreviations.to_csv("../Data/abbreviations.csv", index=False, header=False)
    #print(df)

makeStates()
makeList("../Data/towndata.csv")
