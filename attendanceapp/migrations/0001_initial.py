# Generated by Django 3.2.5 on 2021-08-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=10)),
                ('enrollmentno', models.TextField(max_length=20)),
                ('branch', models.CharField(max_length=5)),
            ],
        ),
    ]