# Generated by Django 4.0.8 on 2023-01-03 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_customuser_firstname_alter_customuser_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='firstname',
            field=models.CharField(default='', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='lastname',
            field=models.CharField(default='', max_length=256, null=True),
        ),
    ]
