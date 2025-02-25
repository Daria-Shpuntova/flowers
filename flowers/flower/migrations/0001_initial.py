# Generated by Django 5.1.4 on 2025-01-01 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='example/')),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('popularity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Семейство',
                'verbose_name_plural': 'Семейства',
            },
        ),
        migrations.CreateModel(
            name='Kingdom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='kingdom/')),
            ],
            options={
                'verbose_name': 'Царство',
                'verbose_name_plural': 'Царства',
            },
        ),
        migrations.CreateModel(
            name='PopularSort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='popular_sort/')),
            ],
            options={
                'verbose_name': 'Популярный сорт',
                'verbose_name_plural': 'Популярные сорта',
            },
        ),
        migrations.CreateModel(
            name='PopularSubspecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='popular_subspecies/')),
            ],
            options={
                'verbose_name': 'Популярный подвид',
                'verbose_name_plural': 'Популярные подвиды',
            },
        ),
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('popularity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.family')),
            ],
            options={
                'verbose_name': 'Род',
                'verbose_name_plural': 'Роды',
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('popularity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('kingdom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.kingdom')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('popularity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.division')),
            ],
            options={
                'verbose_name': 'Порядок',
                'verbose_name_plural': 'Порядки',
            },
        ),
        migrations.AddField(
            model_name='family',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.orders'),
        ),
        migrations.CreateModel(
            name='PopularDivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='popular_division/')),
                ('kingdom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.kingdom')),
            ],
            options={
                'verbose_name': 'Популярный отдел',
                'verbose_name_plural': 'Популярные отделы',
            },
        ),
        migrations.CreateModel(
            name='PopularDivisionName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('popular_division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.populardivision')),
            ],
            options={
                'verbose_name': 'Название представителя популярного отдела',
                'verbose_name_plural': 'Название представителей популярных отделов',
            },
        ),
        migrations.CreateModel(
            name='PopularFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='popular_family/')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.orders')),
            ],
            options={
                'verbose_name': 'Популярное семейство',
                'verbose_name_plural': 'Популярные семейства',
            },
        ),
        migrations.CreateModel(
            name='PopularFamilyName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('popular_family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.popularfamily')),
            ],
            options={
                'verbose_name': 'Название представителя популярного семейства',
                'verbose_name_plural': 'Название представителей популярных семейств',
            },
        ),
        migrations.CreateModel(
            name='PopularGenus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='popular_genus/')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.family')),
            ],
            options={
                'verbose_name': 'Популярный род',
                'verbose_name_plural': 'Популярные роды',
            },
        ),
        migrations.CreateModel(
            name='PopularGenusName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('popular_genus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.populargenus')),
            ],
            options={
                'verbose_name': 'Название представителя популярного рода',
                'verbose_name_plural': 'Название представителей популярных родов',
            },
        ),
        migrations.CreateModel(
            name='PopularOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='popular_orders/')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.division')),
            ],
            options={
                'verbose_name': 'Популярный порядок',
                'verbose_name_plural': 'Популярные порядки',
            },
        ),
        migrations.CreateModel(
            name='PopularOrdersName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('popular_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.popularorders')),
            ],
            options={
                'verbose_name': 'Название представителя популярного порядка',
                'verbose_name_plural': 'Название представителей популярных порядков',
            },
        ),
        migrations.CreateModel(
            name='PopularSortName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('popular_sort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.popularsort')),
            ],
            options={
                'verbose_name': 'Название представителя популярного сорта',
                'verbose_name_plural': 'Название представителей популярных сортов',
            },
        ),
        migrations.CreateModel(
            name='PopularSpecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='popular_species/')),
                ('genus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.genus')),
            ],
            options={
                'verbose_name': 'Популярный вид',
                'verbose_name_plural': 'Популярные виды',
            },
        ),
        migrations.CreateModel(
            name='PopularSpeciesName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('popular_species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.popularspecies')),
            ],
            options={
                'verbose_name': 'Название представителя популярного вида',
                'verbose_name_plural': 'Название представителей популярных видов',
            },
        ),
        migrations.CreateModel(
            name='PopularSubspeciesName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('popular_subspecies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.popularsubspecies')),
            ],
            options={
                'verbose_name': 'Название представителя популярного подвида',
                'verbose_name_plural': 'Название представителей популярных подвидов',
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('popularity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('genus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.genus')),
            ],
            options={
                'verbose_name': 'Вид',
                'verbose_name_plural': 'Виды',
            },
        ),
        migrations.AddField(
            model_name='popularsubspecies',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.species'),
        ),
        migrations.CreateModel(
            name='Subspecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('popularity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.species')),
            ],
            options={
                'verbose_name': 'Подвид',
                'verbose_name_plural': 'Подвиды',
            },
        ),
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('popularity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('subspecies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.subspecies')),
            ],
            options={
                'verbose_name': 'Сорт',
                'verbose_name_plural': 'Сорта',
            },
        ),
        migrations.AddField(
            model_name='popularsort',
            name='subspecies',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.subspecies'),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('characteristics', models.TextField()),
                ('examples', models.ManyToManyField(related_name='types', to='flower.example')),
            ],
        ),
    ]
