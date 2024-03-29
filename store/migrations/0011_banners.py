# Generated by Django 4.1.7 on 2023-05-23 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_dukan_product_image6_dukan_product_image7_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='banners')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banners', to='store.category')),
            ],
            options={
                'verbose_name_plural': 'Banners',
            },
        ),
    ]
