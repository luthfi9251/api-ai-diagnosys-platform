# Generated by Django 4.2.6 on 2023-10-24 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generatedmodelprediction',
            old_name='id_dataset',
            new_name='dataset',
        ),
        migrations.RenameField(
            model_name='generatedmodelprediction',
            old_name='id_model',
            new_name='model',
        ),
    ]
