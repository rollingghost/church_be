# Generated by Django 4.0.8 on 2023-01-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_customuser_firstname_alter_customuser_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='firstname',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='lastname',
            field=models.CharField(max_length=256),
        ),
    ]
