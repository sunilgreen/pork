from lib2to3.pgen2.pgen import DFAState
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from locationdata import makeList
import csv
import random

def getSample(df, col, value, seed, n, positive):
    specificdf = pd.DataFrame([])

    if (positive == True):
        specificdf = df.loc[(df[col].str.contains(value) & df['is_pork'] == 1)]
        print(specificdf)
    else:
        specificdf = df.loc[(df[col].str.contains(value) & df['is_pork'] == 0)]

    datapoints = specificdf.index.tolist() 
    #print(datapoints)
        
    random.seed(seed)
    points = random.sample(datapoints, n)
    points.sort()
    
    #print(sampleFrame)
    row_list = []
    for row in points:
        #print(df.iloc[row,])
        row_list.append(df.iloc[row,])
    
    sampleFrame = pd.DataFrame(row_list)



    return sampleFrame


def preprocess():
    # Binarize committe and subcommittee codes
    df = pd.read_csv("../Data/AllPotentialPork.csv")
    #df = pd.read_csv("../Data/Lazarus2.csv")
    rawData = pd.read_excel("../Data/sampling/garbage.xlsx")
    # df1 = pd.ExcelFile("../Data/Apollo1.xlsx")
    # df = df1.parse(df1, "../Data/Apoll")
    #print(len(rawData))
    
    #Ag-Rural Development-FDA
    agPos = getSample(rawData, "Bill", "Ag-Rural Development-FDA", 11610, 4, True)
    agNeg = getSample(rawData, "Bill", "Ag-Rural Development-FDA", 11610, 21, False)
    #print(agNeg)
    df = pd.concat([agPos, agNeg])
    
    #print(df)

    # #Commerce, Justice & Science
    csjPos = getSample(rawData, "Bill", "Commerce, Justice & Science", 11610, 5, True)
    csjNeg = getSample(rawData, "Bill", "Commerce, Justice & Science", 11610, 34, False)
    df = pd.concat([df, csjPos, csjNeg])
    # #print(df)

    # # #Defense
    defPos = getSample(rawData, "Bill", "Defense", 11610, 6, True)
    defNeg = getSample(rawData, "Bill", "Defense", 11610, 55, False)
    df = pd.concat([df, defPos, defNeg])
    # #print(df)

    # # #Energy & Water
    enwPos = getSample(rawData, "Bill", "Energy & Water", 11610, 4, True)
    enwNeg = getSample(rawData, "Bill", "Energy & Water", 11610, 62, False)
    df = pd.concat([df, enwPos, enwNeg])
    # #print(df)

    # # #Financial Services
    fsPos = getSample(rawData, "Bill", "Financial Services", 11610, 1, True)
    fsNeg = getSample(rawData, "Bill", "Financial Services", 11610, 35, False)
    df = pd.concat([df, fsPos, fsNeg])
    # #print(df)

    # # #Homeland Security 
    hsPos = getSample(rawData, "Bill", "Homeland Security", 11610, 3, True)
    hsNeg = getSample(rawData, "Bill", "Homeland Security", 11610, 4, False)
    df = pd.concat([df, hsPos, hsNeg])

    # # #Interior
    intrPos = getSample(rawData, "Bill", "Interior", 11610, 2, True)
    intrNeg = getSample(rawData, "Bill", "Interior", 11610, 20, False)
    df = pd.concat([df, intrPos, intrNeg])

    # # #Labor-HHS-Education
    lhhsPos = getSample(rawData, "Bill", "Labor-HHS-Education", 11610, 7, True)
    lhhsNeg = getSample(rawData, "Bill", "Labor-HHS-Education", 11610, 60, False)
    df = pd.concat([df, lhhsPos, lhhsNeg])

    # # #Legislative Branch
    lbPos = getSample(rawData, "Bill", "Legislative Branch", 11610, 1, True)
    lbNeg = getSample(rawData, "Bill", "Legislative Branch", 11610, 2, False)
    df = pd.concat([df, lbPos, lbNeg])

    # # #Military Construction
    mcPos = getSample(rawData, "Bill", "Military Construction", 11610, 1, True)
    mcNeg = getSample(rawData, "Bill", "Military Construction", 11610, 80, False)
    df = pd.concat([df, mcPos, mcNeg])
    

    # # #State-Foreign Ops
    sfoPos = getSample(rawData, "Bill", "State-Foreign Ops", 11610, 1, True)
    sfoNeg = getSample(rawData, "Bill", "State-Foreign Ops", 11610, 12, False)
    df = pd.concat([df, sfoPos, sfoNeg])

    # # #Transporation and Housing & Urban Development
    #thudPos = getSample(rawData, "Bill", "Transporation and Housing & Urban Development", 11610, 3, True)
    # thudNeg = getSample(rawData, "Bill", "Transporation and Housing & Urban Development", 11610, 61, False)
    # df = pd.concat([df, thudPos, thudNeg])

    print(len(df))
    print(df)
    
    
    df = df.drop(["ID", "House Request", "Senate Request", "Pre-reduction Amt. (Omni)", "Final Amount", "Budget Request", "Description", "City/Location", "County", "Bill Section", "Bill Subsection", "Project Heading (Defense Bill Only)", "House Requesting Member(s)", "House Party", "House State", "Dist.", "Senate Requesting Member(s)", "Senate Party", "Senate State", "Presidential Earmarks", "Undisclosed", "Intended Recipient or Location", "Notes"], axis=1)
    #df.to_excel("help.xlsx")

    #Analyze the bill text
    #df = analyzeDollarSign(df)
    #df = localityScore(df)
    #cleanText(df, True)
    

    one_hot_encoder_columns = ["State", "Bill"]
    #print(df.columns.values.tolist())

    #Getting rid of raw text
    #df = df.drop(['Text', 'Description'], axis=1)
    #df = df.drop(['State', 'Bill', 'Bill Section', 'Bill Subsection'], axis=1)
    #print(df)

    # Transform sponsor columns into one-hot arrays so decision tree can use categorical variables
    enc = OneHotEncoder(handle_unknown='ignore')
    X = enc.fit_transform(df[one_hot_encoder_columns])

    # Create dataframe with sponsor columns and their corresponding feature titles
    # The new features will be labled as sponsor_party_R, sponsor_party_D, sponsor_state_CA, sponsor_state_AZ, etc.
    #   and will take on binary values
    Xdf = pd.DataFrame(X.toarray(), columns=enc.get_feature_names(one_hot_encoder_columns))

    Xdf.to_excel("../Data/OneHotEncoderCols.xlsx")

    # Combine sponsor dataframe with that of the rest of the data
    #df = df.join(Xdf).drop(['ID'], axis=1)
    df = df.join(Xdf)
    
    # Remove columns made redundant
    df = df.drop(one_hot_encoder_columns, axis=1)
    #df.to_excel("help2.xlsx")
    #df.to_excel("hybrid.xlsx")
    print("-----------------------One Hot Encoder Done-----------------------------------------")

    #df.to_csv("../Data/pretraining.csv")
    # X_data = df.drop(['is_pork'], axis=1) 
    # y_data = df[['is_pork']]

    temp_df = pd.read_excel("./help.xlsx")
    # temp_df.drop(["ID", "State", "Bill"], axis=1)
    X_data = temp_df.drop(['is_pork'], axis=1)
    y_data = temp_df[['is_pork']]

    
    global feature_names 
    feature_names = list(X_data)
    global class_names
    class_names = list(y_data)
    return X_data, y_data

def analyzeDollarSign(df):
    tempdf = df
    local_arr = []
    #Determine whether $ is present
    for i in range(0, len(df)):
        #print(df.iloc[i, 4]) #Note, index where Bill Text is stored
        if (type(df.iloc[i, 4]) != float and "$" in df.iloc[i, 4]):
            #("True at row", i)
            local_arr.append(1)
            # tempdf["locality_score"] = 1
        else:
            #  tempdf["locality_score"] = 0
            local_arr.append(0)
    
    #print(local_arr)
    
    tempdf["has_dollar_sign"] = local_arr
    

    return tempdf

def localityScore(df):
    #Make list of towns
    #makeList("../Data/towndata.csv")
    with open('../Data/specificLocations.csv', newline='') as f:
        reader = csv.reader(f)
        placedata = list(reader)
    
    with open('../Data/states.csv', newline='') as f:
        reader = csv.reader(f)
        statedata = list(reader)
    
    with open('../Data/abbreviations.csv', newline='') as f:
        reader = csv.reader(f)
        abbrevData = list(reader)

    
        
    scores = []

    #Check if text contains one of the districts
    for i in range(0, len(df)):
        score = 0
        for place in placedata:
            if place[0] in df.iloc[i, 4]:
                score += 1
                #print(place[0])
        
        for state in statedata:
            if state[0] in df.iloc[i, 4]:
                score += 0.25
        
        for abbrev in abbrevData:
            if abbrev[0] in df.iloc[i, 4]:
                score += 0.25
        print(score)
        scores.append(score)

    df["locality_score"] = scores
        
    
    return df

def cleanText(df, sentence):
    tempdf = df
    localarr = []
    for i in range(0, len(df)):
        if (sentence):
            tokenized_sent = sent_tokenize(df.iloc([i, 4]))
            #print(tokenized_sent)
    return
