import pandas as pd

def getColValueLength(df, colName, value):
    return len(df[df[colName] == value])


def verifySize(allData):
    print("Incoming length of data frame:", len(allData))
    ag = getColValueLength(allData, "Bill", "Ag-Rural Development-FDA")
    print("Agriculture:", ag)
    csj = getColValueLength(allData, "Bill", "Commerce, Justice & Science")
    print("Commerce, Justice & Science:", csj)
    defense = getColValueLength(allData, "Bill", "Defense")
    print("Defense: ", defense)
    enw = getColValueLength(allData, "Bill", "Energy & Water")
    print("Energy & Water: ", enw)
    fs = getColValueLength(allData, "Bill", "Financial Services")
    print("Financial Services: ", fs)
    hs = getColValueLength(allData, "Bill", "Homeland Security")
    print("Homeland Security: ", hs)
    intr = getColValueLength(allData, "Bill", "Interior")
    print("Interior: ", intr)
    lhhsed = getColValueLength(allData, "Bill", "Labor-HHS-Education")
    print("Labor-HHS-Education: ", lhhsed)
    leg = getColValueLength(allData, "Bill", "Legislative Branch")
    print("Legislative Branch: ", leg)
    mc = getColValueLength(allData, "Bill", "Military Construction")
    print("Military Construction: ", mc)
    sfo = getColValueLength(allData, "Bill", "State-Foreign Ops")
    print("State and Foreign Operations: ", sfo)
    thud = getColValueLength(allData, "Bill", "Transportation and Housing & Urban Development")
    print("THUD: ", thud)
    print("Length of each bill summed together:", ag+csj+defense+enw+fs+hs+intr+lhhsed+leg+mc+sfo+thud)

def createUniqueIds(allData, posPork):
    # for index, row in allData.iterrows():
    #     for index2, row2 in posPork.iterrows():
    newData = pd.concat([allData, posPork], axis=1, join="inner")
    print(len(newData))


def findNegativePork(allData, posPork):


    '''
    Note: It was this effort combined with manual data verification and 
    manipulation in excel that provided the data found in "metphase.xlsx" 
    which was then narrowed down in "garbage.xlsx" and ultimatley used 
    to build the first prototype decision tree

    Further noting, the manual coding process still contained 4 points
    that had both a positive and negative earmark sample. The data loss
    from the manual coding is to be the efforts of further improvement
    in other branches/iterations of this research
    '''
    #Original effort using SQL like logic 
    result = pd.concat([allData, posPork], axis=0, join="inner")
    #result = pd.merge(allData, posPork, on=["Description"])
    print(len(result))
    #result.to_excel("metaphase.xlsx")
    # print(result)
    
    
    #Effort that concats positive pork data at the end, then tries to combine
    #combinedData = pd.concat([allData, posPork], axis=1, ignore_index=True)
    #print(combinedData.iloc[3, ])
    #combinedData.to_excel("anaphase.xlsx")

    #print(posPork.iloc[3,2])
    #Trying to parse through the first part of the data, then the second
    #for index, row in posPork.iterrows():
        #for index2, row2 in allData.iterrows():
            #if (posPork[index][row])

    #     print(combinedData.iloc[i:,])
    
    








allData = pd.read_excel("./TCSEdited.xlsx")
allData.to_csv("TCSCSV.csv")
positivePork = pd.read_csv("./PositivePork.csv")
#print(len(allData))
#verifySize(allData)
#verifySize(positivePork)
realData = pd.read_excel("../garbage.xlsx")
print(realData)

#findNegativePork(allData, positivePork)





