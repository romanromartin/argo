# Generated by Django 4.0.4 on 2022-06-02 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subproduct',
            name='price',
            field=models.CharField(default='0', max_length=60),
        ),
    ]
