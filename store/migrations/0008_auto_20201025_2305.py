# Generated by Django 3.1 on 2020-10-25 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20201025_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Courtwear', 'Courtwear'), ('Accessories', 'Accessories'), ('Ceremonial', 'Ceremonial')], default='Accessories', max_length=20),
        ),
    ]
