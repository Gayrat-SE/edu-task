# Generated by Django 4.0.6 on 2022-08-12 18:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_studentbulkupload_csv_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentbulkupload',
            name='csv_file',
            field=models.FileField(upload_to='students/bulkupload/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'])]),
        ),
    ]