from rest_framework import serializers
from .models import HeartDiseaseDataModel, GeneratedModelPrediction, DatasetModel, ModelPrediction

class HeartDiseaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartDiseaseDataModel
        fields = "__all__"

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetModel
        fields = "__all__"

class ModelPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPrediction
        fields = "__all__"

class GeneratedModelSerializer(serializers.ModelSerializer):
    dataset = DatasetSerializer(many=False)
    model = ModelPredictionSerializer(many=False)
    class Meta:
        model = GeneratedModelPrediction
        fields = "__all__"

class GeneratedModelSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = GeneratedModelPrediction
        fields = "__all__"