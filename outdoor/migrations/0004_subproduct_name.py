# Generated by Django 4.0.4 on 2022-06-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0003_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='subproduct',
            name='name',
            field=models.CharField(default='-', max_length=60),
        ),
    ]
