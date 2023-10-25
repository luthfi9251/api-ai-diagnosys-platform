from django.contrib import admin
from .models import HeartDiseaseDataModel, ModelPrediction, DatasetModel, GeneratedModelPrediction

# Register your models here.
admin.site.register(HeartDiseaseDataModel)
admin.site.register(ModelPrediction)
admin.site.register(DatasetModel)
admin.site.register(GeneratedModelPrediction)