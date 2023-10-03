# Generated by Django 4.2.1 on 2023-10-03 11:57

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
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('full_name', models.CharField(max_length=128, verbose_name='Full name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('is_call', models.BooleanField(default=False, verbose_name='Is for call or on collection?')),
                ('active', models.BooleanField(default=True, verbose_name='Active?')),
                ('on_collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inquires', to='store.collection', verbose_name='On Collection')),
            ],
            options={
                'verbose_name': 'Inquiry on collection',
                'verbose_name_plural': 'Inquiries on collection',
            },
        ),
        migrations.CreateModel(
            name='InquiryCall',
            fields=[
            ],
            options={
                'verbose_name': 'Inquiry for call',
                'verbose_name_plural': 'Inquiries for call',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('inquiries.inquiry',),
        ),
    ]
