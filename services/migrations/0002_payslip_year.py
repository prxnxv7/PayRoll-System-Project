# Generated by Django 3.2.20 on 2023-09-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip',
            name='year',
            field=models.IntegerField(default=2023),
        ),
    ]
