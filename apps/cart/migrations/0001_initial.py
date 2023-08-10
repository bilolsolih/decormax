# Generated by Django 4.2.3 on 2023-08-09 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='Device id')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Quantity')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=24, verbose_name='Cost')),
                ('articul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.articul', verbose_name='Articul')),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.cart', verbose_name='Cart')),
                ('collection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.collection', verbose_name='Collection')),
            ],
            options={
                'verbose_name': 'Cart item',
                'verbose_name_plural': 'Cart items',
            },
        ),
    ]
