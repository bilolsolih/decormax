# Generated by Django 4.2.3 on 2023-08-05 09:59

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_price'),
        ('inquiries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='on_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inquires', to='store.product', verbose_name='about product'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone number'),
        ),
    ]