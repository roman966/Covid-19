# Generated by Django 3.1.1 on 2020-09-30 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.IntegerField(null=True)),
                ('Sex', models.CharField(max_length=20, null=True)),
                ('Temparature', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('Assessment_Date', models.DateTimeField(auto_now_add=True)),
                ('Assessment_Score', models.IntegerField(null=True)),
                ('Result', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
