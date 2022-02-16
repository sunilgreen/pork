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




def preprocess():

    # Binarize committe and subcommittee codes
    # df = pd.read_csv("../Data/AllPotentialPork.csv")
    df = pd.read_csv("../Data/Lazarus2.csv")
    # df1 = pd.ExcelFile("../Data/Apollo1.xlsx")
    # df = df1.parse(df1, "../Data/Apoll")
    print(df)
    df = df.drop(["Final Amount"], axis=1)


    #Analyze the bill text
    #df = analyzeDollarSign(df)
    #df = localityScore(df)

    #cleanText(df, True)

    
    
    

    one_hot_encoder_columns = ['State', 'Bill', 'Bill Section']
    print(df.columns.values.tolist())

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
    df = df.join(Xdf).drop(['ID'], axis=1)
    
    # Remove columns made redundant
    df = df.drop(one_hot_encoder_columns, axis=1)
    print("------------------------------------------------------------------------------")
    print(df)

    df.to_csv("../Data/pretraining.csv")
    X_data = df.drop(['is_pork'], axis=1) 
    y_data = df[['is_pork']]
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
