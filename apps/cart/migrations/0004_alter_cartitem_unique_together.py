# Generated by Django 4.2.1 on 2023-08-22 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_collection_title_en_and_more'),
        ('cart', '0003_alter_cartitem_articul'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'collection', 'device_id')},
        ),
    ]
