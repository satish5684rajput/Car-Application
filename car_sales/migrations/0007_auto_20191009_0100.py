# Generated by Django 2.2.6 on 2019-10-08 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_sales', '0006_auto_20191009_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesrecords',
            name='sales_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
