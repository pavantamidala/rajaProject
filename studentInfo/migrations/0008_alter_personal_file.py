# Generated by Django 3.2 on 2021-05-03 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentInfo', '0007_personal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='file',
            field=models.ImageField(default='default', upload_to='photos/'),
        ),
    ]