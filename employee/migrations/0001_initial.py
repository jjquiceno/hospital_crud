# Generated by Django 3.2.7 on 2021-10-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.CharField(max_length=254)),
                ('econtact', models.CharField(max_length=250)),
                ('edistri', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
