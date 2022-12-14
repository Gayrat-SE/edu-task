# Generated by Django 4.0.6 on 2022-08-12 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_last_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentBulkUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('date_uploaded', models.DateTimeField(auto_now=True)),
                ('csv_file', models.FileField(upload_to='students/bulkupload/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
