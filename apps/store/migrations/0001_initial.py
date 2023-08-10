# Generated by Django 4.2.3 on 2023-08-09 12:41

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='BuildingMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=128, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=128, null=True, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=128, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materials',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=128, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=128, null=True, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=128, null=True, verbose_name='Title')),
                ('photo', models.ImageField(upload_to='images/store/collections/%Y/%m/%d', verbose_name='Photo')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_ru', models.TextField(null=True, verbose_name='Description')),
                ('description_en', models.TextField(null=True, verbose_name='Description')),
                ('description_uz', models.TextField(null=True, verbose_name='Description')),
                ('no_in_pack', models.PositiveIntegerField(verbose_name='Number in a pack')),
                ('status', models.CharField(blank=True, choices=[('Hit', 'Hit'), ('New', 'New'), ('Sale', 'Sale')], max_length=4, null=True, verbose_name='Status')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('active', models.BooleanField(default=True, verbose_name='Is active')),
                ('brand', models.ManyToManyField(related_name='products', to='store.brand', verbose_name='Brand')),
                ('building_material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='store.buildingmaterial', verbose_name='Building material')),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('hexa_value', models.CharField(max_length=24, verbose_name='Hexa Value')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='ManufacturingMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=128, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=128, null=True, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=128, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Manufacturing method',
                'verbose_name_plural': 'Manufacturing methods',
            },
        ),
        migrations.CreateModel(
            name='PictureType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=128, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=128, null=True, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=128, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Picture type',
                'verbose_name_plural': 'Picture types',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Width length')),
                ('height', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Height length')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='UZ', verbose_name='Phone number')),
                ('region', models.CharField(max_length=128, verbose_name='Region')),
                ('district', models.CharField(max_length=128, verbose_name='City or district')),
                ('address', models.CharField(max_length=256, verbose_name='Address')),
                ('orient', models.CharField(blank=True, max_length=256, null=True, verbose_name='Orient')),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=128, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=128, null=True, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=128, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Style',
                'verbose_name_plural': 'Styles',
            },
        ),
        migrations.CreateModel(
            name='TargetRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=128, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=128, null=True, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=128, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Target room',
                'verbose_name_plural': 'Target rooms',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('video', models.FileField(upload_to='videos/store/articuls/%Y/%m/%d', verbose_name='Video file')),
                ('photo', models.ImageField(upload_to='videos/store/articuls/%Y/%m/%d', verbose_name='Photo')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='store.collection', verbose_name='Collection')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.AddField(
            model_name='collection',
            name='color',
            field=models.ManyToManyField(related_name='products', to='store.color', verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='collection',
            name='manufacturing_method',
            field=models.ManyToManyField(related_name='products', to='store.manufacturingmethod', verbose_name='Manufacture method'),
        ),
        migrations.AddField(
            model_name='collection',
            name='picture_type',
            field=models.ManyToManyField(related_name='products', to='store.picturetype', verbose_name='Picture type'),
        ),
        migrations.AddField(
            model_name='collection',
            name='size',
            field=models.ManyToManyField(related_name='products', to='store.size', verbose_name='Size'),
        ),
        migrations.AddField(
            model_name='collection',
            name='style',
            field=models.ManyToManyField(related_name='products', to='store.style', verbose_name='Style'),
        ),
        migrations.AddField(
            model_name='collection',
            name='target_room',
            field=models.ManyToManyField(related_name='products', to='store.targetroom', verbose_name='Target room'),
        ),
        migrations.CreateModel(
            name='Articul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('photo', models.ImageField(upload_to='images/store/articuls/%Y/%m/%d', verbose_name='Photo')),
                ('collection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articuls', to='store.collection', verbose_name='Collection')),
            ],
            options={
                'verbose_name': 'Articul',
                'verbose_name_plural': 'Articuls',
            },
        ),
    ]
