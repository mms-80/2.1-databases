# Generated by Django 5.0.2 on 2024-03-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.CharField(max_length=254)),
                ('release_date', models.CharField(max_length=10)),
                ('lte_exists', models.BooleanField()),
            ],
        ),
    ]