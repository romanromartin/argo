# Generated by Django 4.0.4 on 2022-06-07 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0005_subproduct_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(default='-', max_length=60)),
                ('phone', models.CharField(default='-', max_length=10)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
