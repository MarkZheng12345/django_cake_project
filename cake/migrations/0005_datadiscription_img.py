# Generated by Django 4.1.7 on 2023-02-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0004_rename_datadiscription3_datadiscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='datadiscription',
            name='img',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
    ]