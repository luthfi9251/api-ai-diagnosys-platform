# Generated by Django 4.2.6 on 2023-10-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_heartdiseasedatamodel_oldpeak'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetmodel',
            name='format_file',
            field=models.CharField(default='.csv', max_length=10),
        ),
        migrations.AddField(
            model_name='datasetmodel',
            name='target_label',
            field=models.CharField(default='-', max_length=20),
        ),
    ]