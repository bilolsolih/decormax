# Generated by Django 4.2.1 on 2023-09-27 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0001_initial'),
    ]

    operations = [
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
        migrations.AlterModelOptions(
            name='inquiry',
            options={'verbose_name': 'Inquiry on collection', 'verbose_name_plural': 'Inquiries on collection'},
        ),
        migrations.AddField(
            model_name='inquiry',
            name='is_call',
            field=models.BooleanField(default=False, verbose_name='Is for call or on collection?'),
        ),
    ]