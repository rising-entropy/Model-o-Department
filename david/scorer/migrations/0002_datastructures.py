# Generated by Django 3.1.1 on 2020-09-13 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataStructures',
            fields=[
                ('id', models.Field(primary_key=True, serialize=False)),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
    ]
