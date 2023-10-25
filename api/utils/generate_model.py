import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix

'''
    Argumen model berisi
    {
        model_algorithm: "Decision Tree".
        parameter:{
            criterion: "clf_gini",
            max_depth: 2,
            min_samples_leaf: 4,
            min_samples_split: 3,
            random_state:242
        }
    }

    Argumen Dataset berisi
    {
        nama_dataset: "aasa",
        test_size: 0.1,
        target_label: "output",
        format_file: "xls"
    }
'''

def generate_model(model, dataset):
    df = None
    path_to_model = os.path.join(os.getcwd(),"api\prediction\dataset",f"{dataset['nama_dataset']}.{dataset['format_file']}")
    df = pd.read_csv(path_to_model)

    label_target = dataset["target_label"]
    y=df[[label_target]]
    x=df.drop(label_target,axis=1)
    x_train , x_test , y_train , y_test = train_test_split(x,y, test_size=dataset["test_size"], random_state=0)

    model_prediction = None

    if model["model_algorithm"] == "decision_tree":
        model_prediction = DecisionTreeClassifier(**model["parameter"])
    
    if model_prediction is None:
        return {
            "success": False,
            "message": "model algorithm not found"
        }

    
    model_prediction.fit(x_train, y_train)
    y_pred = model_prediction.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    result_dict = {
        "succes": True,
        "model_algorithm" : model["model_algorithm"],
        "parameter": model["parameter"],
        "dataset": dataset["nama_dataset"],
        "test_size": dataset["test_size"],
        "accuracy": accuracy,
        "recall": recall,
        "confusion_matrix": confusion_matrix(y_test, y_pred)
    }

    return result_dict

model_dict = {
    "model_algorithm": "decision_tree",
    "parameter":{
        "criterion": "entropy",
        "max_depth": 2,
        "min_samples_leaf": 4,
        "min_samples_split": 3,
        "random_state":242
    }
}

dataser_dict = {
    "nama_dataset": "heart_disease_small",
    "test_size": 0.1,
    "target_label": "output",
    "format_file": "xls"
}

#print(generate_model(model_dict,dataser_dict))