# Generated by Django 4.0.5 on 2022-07-13 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_homework_homework_text_alter_homework_homework_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeworksubmission',
            name='submission_rating',
            field=models.IntegerField(blank=True, max_length=5),
        ),
    ]