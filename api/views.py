from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HeartDiseaseModelSerializer, GeneratedModelSerializer, DatasetSerializer, ModelPredictionSerializer, GeneratedModelSerializerWrite
from .models import HeartDiseaseDataModel, GeneratedModelPrediction, DatasetModel, ModelPrediction
from .utils import prediction, generate_model
import numpy as np

# Create your views here.
class HeartDiseaseView(APIView):
    serializer_class = HeartDiseaseModelSerializer

    def get(self, request, *args, **kwargs):
        history = HeartDiseaseDataModel.objects.all()
        serializer = HeartDiseaseModelSerializer(history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data_to_predict = {
        "age": request.data["age"],
        "sex": request.data["sex"],
        "cp": request.data["cp"],
        "trtbps": request.data["trtbps"],
        "chol": request.data["chol"],
        "fbs": request.data["fbs"],
        "restecg": request.data["restecg"],
        "thalachh": request.data["thalachh"],
        "exng": request.data["exng"],
        "oldpeak": request.data["oldpeak"],
        "slp": request.data["slp"],
        "caa": request.data["caa"],
        "thall": request.data["thall"]
        }

        result = prediction.predict_data(data_to_predict,"HeartDisease-SmallDataset").flatten().tolist()
        data_to_predict["output"] = result.index(max(result))
        

        serializer = HeartDiseaseModelSerializer(data=data_to_predict)
        #print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": {
                "resultInt": result.index(max(result)),
                "resultText": "positive" if result.index(max(result)) == 1 else "negative",
                "confidenceValue": result
                }
                }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ModelInformation(APIView):
    serializer_class = GeneratedModelSerializerWrite

    def get(self, request, *args, **kwargs):
        id_model = request.query_params.get("id")
        model_name = request.query_params.get("name")
        kategori_model = request.query_params.get("kategori")
        
        model_info = GeneratedModelPrediction.objects.all()

        if id_model is not None:
            model_info = GeneratedModelPrediction.objects.filter(id=id_model)
        
        if model_name is not None:
            model_info = GeneratedModelPrediction.objects.filter(nama_model=model_name)
        
        if kategori_model is not None:
            model_info = GeneratedModelPrediction.objects.filter(kategori_model=kategori_model)
        
        serializer = GeneratedModelSerializer(model_info, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = GeneratedModelSerializerWrite(data=request.data)
        #print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":"Model Data berhasil disimpan"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ModelGenerator(APIView):
    def get(self, request):
        dataset_info = DatasetModel.objects.all()
        prediction_model = ModelPrediction.objects.all()

        serializer_dataset = DatasetSerializer(dataset_info, many=True)
        serializer_model_prediction = ModelPredictionSerializer(prediction_model, many=True)

        return Response({"data": {
            "dataset": serializer_dataset.data,
            "model" : serializer_model_prediction.data
        }}, status=status.HTTP_200_OK)
        pass
    def post(self, request):
        id_model = request.data["id_model"]
        id_dataset = request.data["id_dataset"]

        serializer_model = ModelPredictionSerializer(ModelPrediction.objects.get(id_model=id_model))
        serializer_dataset = DatasetSerializer(DatasetModel.objects.get(id_dataset=id_dataset))

        model_dict = {
            "model_algorithm": serializer_model.data["model_algorithm"],
            "parameter":{ **request.data["parameter"] }
        }

        dataset_dict = {
            "nama_dataset": serializer_dataset.data["nama_dataset"],
            "test_size": request.data["test_size"],
            "target_label": serializer_dataset.data["target_label"],
            "format_file": serializer_dataset.data["format_file"]
        }

        return Response({"data": generate_model.generate_model(model_dict,dataset_dict)}, status=status.HTTP_200_OK)

