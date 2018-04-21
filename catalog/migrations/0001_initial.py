# Generated by Django 2.0.4 on 2018-04-20 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price_rub', models.IntegerField(verbose_name='Price in rubles')),
                ('product_image', models.FileField(upload_to='')),
                ('in_store', models.BooleanField(default=False)),
                ('departments', models.ManyToManyField(related_name='products', to='catalog.Department')),
                ('features', models.ManyToManyField(blank=True, to='catalog.Feature')),
            ],
        ),
    ]