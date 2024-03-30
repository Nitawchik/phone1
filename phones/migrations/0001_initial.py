# Generated by Django 4.2 on 2023-05-05 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.CharField(max_length=250)),
                ('release_date', models.CharField(max_length=10)),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
