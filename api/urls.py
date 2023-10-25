from .views import HeartDiseaseView, ModelInformation, ModelGenerator
from django.urls import path

urlpatterns = [
    path("heartdisease",HeartDiseaseView.as_view()),
    path("model/info", ModelInformation.as_view()),
    path("model/generate", ModelGenerator.as_view())
]