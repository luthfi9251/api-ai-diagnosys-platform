import pandas as pd
import pickle
import os


def predict_data(data, model_name):
    current_file_path = os.getcwd()
    model_folder_path = os.path.join(current_file_path,"api\prediction\model")
    data_dataframe = pd.DataFrame(data,index=[0])
    

    loaded_model = pickle.load(open(os.path.join(model_folder_path,f"{model_name}.sav"),'rb'))

    
    return loaded_model.predict_proba(data_dataframe)
    