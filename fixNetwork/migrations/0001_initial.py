# Generated by Django 5.0.7 on 2024-08-25 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fixnetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('router', models.CharField(max_length=200)),
                ('m14', models.CharField(max_length=200)),
                ('m10', models.CharField(max_length=200)),
            ],
        ),
    ]
