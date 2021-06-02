# Generated by Django 3.2.3 on 2021-05-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20201130_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=8)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Comptoir', 'Comptoir'), ('Machine', 'Machine'), ('Vitrine', 'Vitrine'), ('Mirale', 'Mirale'), ('Serie', 'Serie')], default='serie', max_length=20),
        ),
    ]