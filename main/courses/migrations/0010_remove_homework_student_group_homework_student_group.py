# Generated by Django 4.0.5 on 2022-07-19 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('courses', '0009_alter_homework_student_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='student_group',
        ),
        migrations.AddField(
            model_name='homework',
            name='student_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='groups', to='user.studentgroup'),
        ),
    ]