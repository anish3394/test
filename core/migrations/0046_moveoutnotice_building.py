# Generated by Django 4.0.2 on 2022-03-23 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental_property', '0015_alter_maintanancenotice_maintanance_status'),
        ('core', '0045_unittour_building'),
    ]

    operations = [
        migrations.AddField(
            model_name='moveoutnotice',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rental_property.building'),
        ),
    ]
