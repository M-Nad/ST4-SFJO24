import pickle
import pandas as pd
#from ML_model import train_model

matrix_df =  pd.read_csv("Database/Dataset_credibility/matrix_4.csv")
model_name= "model_2.0"

def get_model():
    """
    Function to call to get the model and predict if a tweet (list of 0 and 1 matching the features list) is a fake news or not 
    RETURN : a model object and the list of model's rules fro the tweet conversion in list of 0 and 1
    """
    #metrics = train_model(matrix, model_name)
    features = matrix_df.columns.tolist()[2:]
    with open('ML_models/'+ model_name, 'rb') as training_model:
        model = pickle.load(training_model)
    return model, features
