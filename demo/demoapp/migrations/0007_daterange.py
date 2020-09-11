# Generated by Django 3.1 on 2020-09-02 21:36

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
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('date_time', models.DateTimeField()),
            ],
        ),
    ]