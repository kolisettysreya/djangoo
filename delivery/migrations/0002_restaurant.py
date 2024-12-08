# Generated by Django 5.1.1 on 2024-12-05 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('delivery_time', models.CharField(max_length=20)),
                ('cuisine', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('discount', models.CharField(max_length=50)),
            ],
        ),
    ]
