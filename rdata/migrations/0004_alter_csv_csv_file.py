# Generated by Django 4.1.3 on 2022-11-07 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdata', '0003_alter_data_adj_close_alter_data_close_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='csv_file',
            field=models.FileField(unique=True, upload_to=''),
        ),
    ]