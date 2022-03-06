# Generated by Django 4.0.2 on 2022-02-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities_and_rent', '0004_alter_unitrentdetails_amount_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitrentdetails',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='unitrentdetails',
            name='amount_paid_in_advance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]