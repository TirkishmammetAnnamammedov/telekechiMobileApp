# Generated by Django 4.0.5 on 2023-04-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_about_product_product_product_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dukan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=70)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product')),
                ('product_image2', models.ImageField(blank=True, null=True, upload_to='product')),
                ('product_image3', models.ImageField(blank=True, null=True, upload_to='product')),
                ('product_image4', models.ImageField(blank=True, null=True, upload_to='product')),
                ('product_image5', models.ImageField(blank=True, null=True, upload_to='product')),
                ('product_address', models.CharField(max_length=100)),
                ('product_quantity', models.CharField(max_length=8)),
                ('product_description', models.TextField(blank=True)),
                ('delivery', models.BooleanField(default=False)),
                ('credit', models.BooleanField(default=False)),
                ('joined_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Dukan',
            },
        ),
    ]
