# Generated by Django 4.0.5 on 2022-07-11 16:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0018_student_education_start_date_teacher_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('homework_title', models.CharField(max_length=255)),
                ('homework_file', models.FileField(upload_to='homeworks/')),
                ('homework_created_time', models.DateTimeField(auto_now_add=True)),
                ('homework_deadline_time', models.DateTimeField(null=True)),
                ('student_group', models.ManyToManyField(to='user.studentgroup')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.teacher')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomeworkSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('upload_homework_time', models.DateTimeField(auto_now_add=True)),
                ('submission_homework_file', models.FileField(blank=True, upload_to='answers/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'ppt'])])),
                ('submission_rating', models.FloatField(blank=True)),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.homework')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]