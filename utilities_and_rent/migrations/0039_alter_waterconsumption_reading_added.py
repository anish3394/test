# Generated by Django 4.0.2 on 2022-03-03 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities_and_rent', '0038_alter_waterbilling_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterconsumption',
            name='reading_added',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]