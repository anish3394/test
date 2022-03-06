# Generated by Django 4.0.2 on 2022-03-01 16:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('utilities_and_rent', '0030_rename_water_waterbilling_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='electricity',
            options={'verbose_name_plural': 'Billing | Electricity'},
        ),
        migrations.AlterModelOptions(
            name='waterbilling',
            options={'verbose_name_plural': 'Billing | Water '},
        ),
        migrations.AddField(
            model_name='waterbilling',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]