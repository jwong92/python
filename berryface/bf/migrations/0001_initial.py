# Generated by Django 2.0.6 on 2018-06-06 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=300)),
                ('temp', models.IntegerField(verbose_name='temperature')),
                ('pub_date', models.DateTimeField(verbose_name='date pulled')),
            ],
        ),
    ]
