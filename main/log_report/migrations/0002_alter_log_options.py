# Generated by Django 4.0.6 on 2022-09-09 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log_report', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'ordering': ('-created_at',)},
        ),
    ]
