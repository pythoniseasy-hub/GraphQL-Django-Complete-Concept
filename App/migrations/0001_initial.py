# Generated by Django 3.1.4 on 2020-12-26 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Duration', models.CharField(max_length=5)),
                ('Published_at', models.DateField(auto_now_add=True)),
                ('singer', models.ManyToManyField(to='App.Singer')),
            ],
        ),
    ]
