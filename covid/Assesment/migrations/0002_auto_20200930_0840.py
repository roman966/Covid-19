# Generated by Django 3.1.1 on 2020-09-30 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assesment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Assessment_Date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='Temparature',
            field=models.IntegerField(null=True),
        ),
    ]