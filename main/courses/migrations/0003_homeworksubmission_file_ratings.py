# Generated by Django 4.0.5 on 2022-07-24 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_homeworksubmission_submission_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeworksubmission',
            name='file_ratings',
            field=models.FileField(blank=True, upload_to='ratings/'),
        ),
    ]