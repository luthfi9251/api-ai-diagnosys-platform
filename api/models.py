from django.db import models

# Create your models here.

# Kelas untuk menyimpan data prediksi Heart Disease Prediction
class HeartDiseaseDataModel(models.Model):
    '''
    {'age': 42,
    'sex': 1,
    'cp': 3,
    'trtbps': 145,
    'chol': 130,
    'fbs': 1,
    'restecg': 0,
    'thalachh': 120,
    'exng': 1,
    'oldpeak': 1.0,
    'slp': 2,
    'caa': 0,
    'thall': 0}
    '''

    age = models.IntegerField(default=0)
    sex = models.IntegerField(choices=[(0,"Male"),(1,"Female")])
    cp = models.IntegerField(default=0)
    trtbps = models.IntegerField(default=0)
    chol = models.IntegerField(default=0)
    fbs = models.IntegerField(default=0)
    restecg = models.IntegerField(default=0)
    thalachh = models.IntegerField(default=0)
    exng = models.IntegerField(default=0)
    oldpeak = models.FloatField(default=0)
    slp = models.IntegerField(default=0)
    caa = models.IntegerField(default=0)
    thall = models.IntegerField(default=0)
    output = models.IntegerField(default=-1)

class DatasetModel(models.Model):
    id_dataset = models.AutoField(primary_key=True)
    nama_dataset = models.CharField(max_length=100)
    kategori_dataset = models.CharField(max_length=50, choices=[("heart_disease", "Heart Disease"),("stroke","Stroke")])
    link_dataset = models.CharField(max_length=250)
    field_count = models.IntegerField(default=0)
    field_list = models.TextField(null=True)
    data_count = models.IntegerField(default=0)
    format_file = models.CharField(max_length=10,default=".csv")
    target_label = models.CharField(max_length=20, default="-")

class ModelPrediction(models.Model):
    id_model = models.AutoField(primary_key=True)
    model_algorithm = models.CharField(max_length=50, choices=[("decision_tree","Decision Tree")], default="decision_tree")
    parameter_count = models.IntegerField(default=0)
    parameter_list = models.TextField(null=True)

class GeneratedModelPrediction(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.ForeignKey(ModelPrediction, on_delete=models.CASCADE, related_name="model_type")
    dataset = models.ForeignKey(DatasetModel, on_delete=models.CASCADE, related_name="dataset")
    nama_model = models.CharField(max_length=50)
    kategori_model = models.CharField(max_length=50)
    akurasi = models.FloatField()
    recall = models.FloatField()
    path_model = models.CharField(max_length=50)
