# Generated by Django 4.2.7 on 2024-03-03 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_doctormodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='departmentmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
