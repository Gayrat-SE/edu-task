# Generated by Django 4.0.5 on 2022-07-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_studentgroup_student_studentgroup_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.CharField(blank=True, max_length=22, null=True),
        ),
    ]
