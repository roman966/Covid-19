# Generated by Django 3.1.1 on 2020-09-30 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Assesment', '0002_auto_20200930_0840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='Temparature',
            new_name='Temp',
        ),
    ]
