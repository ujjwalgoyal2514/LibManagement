# Generated by Django 4.2.7 on 2023-12-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0002_auto_20230911_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
