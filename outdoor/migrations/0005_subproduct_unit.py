# Generated by Django 4.0.4 on 2022-06-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0004_subproduct_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subproduct',
            name='unit',
            field=models.CharField(default='-', max_length=60),
        ),
    ]