# Generated by Django 4.0.5 on 2023-04-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_client_groups_client_user_permissions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]