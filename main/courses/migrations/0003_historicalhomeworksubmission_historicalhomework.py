# Generated by Django 4.0.6 on 2022-09-09 12:11

import courses.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_studentbulkupload_csv_file'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_alter_homeworksubmission_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalHomeworkSubmission',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateField(blank=True, editable=False)),
                ('deleted_at', models.DateField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('upload_homework_time', models.DateTimeField(blank=True, editable=False)),
                ('submission_homework_file', models.TextField(blank=True, max_length=100, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'ppt'])])),
                ('submission_rating', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('is_answered', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('homework', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='courses.homework')),
                ('student', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.student')),
            ],
            options={
                'verbose_name': 'historical homework submission',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalHomework',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateField(blank=True, editable=False)),
                ('deleted_at', models.DateField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('homework_title', models.CharField(max_length=255)),
                ('homework_text', models.TextField(blank=True)),
                ('homework_file', models.TextField(max_length=100)),
                ('homework_created_time', models.DateTimeField(blank=True, editable=False, null=True)),
                ('homework_deadline_time', models.DateTimeField(validators=[courses.models.deadline_time])),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('student_group', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.studentgroup')),
                ('teacher', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.teacher')),
            ],
            options={
                'verbose_name': 'historical homework',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]