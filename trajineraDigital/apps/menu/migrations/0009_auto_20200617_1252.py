# Generated by Django 3.0.3 on 2020-06-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20200617_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='precio_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
