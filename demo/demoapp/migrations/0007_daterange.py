# Generated by Django 3.1 on 2020-09-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0006_inputmask'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_range', models.CharField(max_length=25)),
                ('date_custom', models.CharField(max_length=25)),
                ('date_time', models.CharField(max_length=40)),
            ],
        ),
    ]
