# Generated by Django 5.1.1 on 2024-12-05 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_homedeliveryitem_onlinebookingitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HomeDeliveryItem',
        ),
        migrations.DeleteModel(
            name='OnlineBookingItem',
        ),
    ]
