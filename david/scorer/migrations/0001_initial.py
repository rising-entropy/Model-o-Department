# Generated by Django 3.1.1 on 2020-09-13 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerOrganisationArchitecture',
            fields=[
                ('id', models.Field(primary_key=True, serialize=False)),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='DataCommunication',
            fields=[
                ('id', models.Field(primary_key=True, serialize=False)),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='DiscreteMath',
            fields=[
                ('id', models.Field(primary_key=True, serialize=False)),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ProbabilityAndStatistics',
            fields=[
                ('id', models.Field(primary_key=True, serialize=False)),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareEngineering',
            fields=[
                ('id', models.Field(primary_key=True, serialize=False)),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.Field(primary_key=True, serialize=False)),
                ('fName', models.CharField(max_length=50)),
                ('lName', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.Field(primary_key=True, serialize=False)),
                ('fName', models.CharField(max_length=50)),
                ('lName', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
    ]