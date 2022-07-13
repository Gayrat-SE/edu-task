# Generated by Django 4.0.5 on 2022-07-13 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_alter_studentgroup_student'),
        ('courses', '0009_alter_homeworkanswer_answer_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeworkstudent',
            name='student',
        ),
        migrations.RemoveField(
            model_name='homeworkstudent',
            name='teacher',
        ),
        migrations.AddField(
            model_name='homework',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.student'),
        ),
        migrations.DeleteModel(
            name='HomeworkAnswer',
        ),
        migrations.DeleteModel(
            name='HomeworkStudent',
        ),
    ]