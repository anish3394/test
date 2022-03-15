# Generated by Django 4.0.2 on 2022-03-14 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental_property', '0009_remove_maintanancenotice_unit'),
        ('complaints', '0012_helpcontacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpcontacts',
            name='associated_building',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rental_property.building'),
            preserve_default=False,
        ),
    ]
