# Generated by Django 3.1.7 on 2021-05-08 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triaje', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionaria',
            name='celular',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='usuaria',
            name='celular',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
