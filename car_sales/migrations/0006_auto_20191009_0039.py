# Generated by Django 2.2.6 on 2019-10-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_sales', '0005_auto_20191005_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesrecords',
            name='Matt_finish',
            field=models.CharField(choices=[('Yes', 1), ('No', 0)], max_length=1),
        ),
        migrations.AlterField(
            model_name='salesrecords',
            name='air_bugs',
            field=models.CharField(choices=[('Yes', 1), ('No', 0)], max_length=1),
        ),
        migrations.AlterField(
            model_name='salesrecords',
            name='music_system',
            field=models.CharField(choices=[('Yes', 1), ('No', 0)], max_length=1),
        ),
        migrations.AlterField(
            model_name='salesrecords',
            name='power_steering',
            field=models.CharField(choices=[('Yes', 1), ('No', 0)], max_length=1),
        ),
        migrations.AlterField(
            model_name='salesrecords',
            name='sun_roof',
            field=models.CharField(choices=[('Yes', 1), ('No', 0)], max_length=1),
        ),
    ]
