# Generated by Django 4.2.1 on 2023-09-29 09:40

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128, verbose_name='Full name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='UZ', verbose_name='Phone number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('delivery_type', models.CharField(choices=[('s', 'Self-picked'), ('d', 'Delivery')], max_length=1, verbose_name='Delivery type')),
                ('final_price', models.DecimalField(decimal_places=2, default=0, max_digits=24, verbose_name='Final price')),
                ('city', models.CharField(blank=True, max_length=128, null=True, verbose_name='Destination city')),
                ('region', models.CharField(blank=True, max_length=128, null=True, verbose_name='Region')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name='Address')),
                ('level', models.CharField(blank=True, max_length=128, null=True, verbose_name='Floor number')),
                ('delivery_date', models.DateField(blank=True, null=True, verbose_name='Delivery date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('status', models.CharField(choices=[('d', 'Delivered'), ('p', 'Pending')], default='p', max_length=1, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=128, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=128, null=True, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=128, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Payment type',
                'verbose_name_plural': 'Payment types',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=24, verbose_name='Cost')),
                ('artikul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='store.articul', verbose_name='Articul')),
                ('collection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='store.collection', verbose_name='Collection')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Order item',
                'verbose_name_plural': 'Order items',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='orders.paymenttype', verbose_name='Payment method'),
        ),
        migrations.AddField(
            model_name='order',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='store.store', verbose_name='Store'),
        ),
    ]
