import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder




def preprocess():
    # Binarize committe and subcommittee codes
    mlb = MultiLabelBinarizer()
    df = pd.read_csv("../Data/MergedWithText.csv")
    df = df.drop(['Text', 'Description'], axis=1)
    print(df)
    

    one_hot_encoder_columns = ['Party', 'State']
    # Transform sponsor columns into one-hot arrays so decision tree can use categorical variables
    enc = OneHotEncoder(handle_unknown='ignore')
    X = enc.fit_transform(df[one_hot_encoder_columns])

    # Create dataframe with sponsor columns and their corresponding feature titles
    # The new features will be labled as sponsor_party_R, sponsor_party_D, sponsor_state_CA, sponsor_state_AZ, etc.
    #   and will take on binary values
    Xdf = pd.DataFrame(X.toarray(), columns=enc.get_feature_names(one_hot_encoder_columns))

    # Combine sponsor dataframe with that of the rest of the data
    df = df.join(Xdf).drop(['ID'], axis=1)
    
    # Remove columns made redundant
    df = df.drop(one_hot_encoder_columns, axis=1)
    print(df)

    X_data = df.drop(['is_pork'], axis=1) 
    y_data = df[['is_pork']]
    global feature_names 
    feature_names = list(X_data)
    global class_names
    class_names = list(y_data)
    return X_data, y_data

