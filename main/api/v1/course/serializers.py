from rest_framework import serializers
from courses.models import Homework, HomeworkSubmission

class CreateHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ('homework_title', 'homework_file', 'homework_created_time', 'homework_deadline_time',
        'teacher', 'student_group')



class SendHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkSubmission
        fields = '__all__'