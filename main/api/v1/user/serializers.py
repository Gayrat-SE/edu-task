from rest_framework import serializers
from user.models import User, Student, Teacher, Admin, StudentGroup


class StudentCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(write_only = True, source='user.password')
    gender = serializers.CharField(source = 'user.gender')
    father_name = serializers.CharField(source='user.father_name')
    birthday = serializers.DateField(source='user.birthday')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    email = serializers.CharField(source = 'user.email')
    image = serializers.ImageField(source = 'user.image')
    phone = serializers.CharField(source = 'user.phone')
    class Meta:
        model = Student
        fields = ('username', 'password', 'gender', 'father_name', 'birthday', 'first_name', 'last_name', 'email', 'image', 'phone')

    def create(self, validated_data):
        user = validated_data.pop('user')
        user = User.objects.create(username=user['username'], first_name = user['first_name'],
            email = user['email'], gender= user['gender'],  birthday = user['birthday'], father_name = user['father_name'],
            last_name = user['last_name'], image = user['image'], phone = user['phone']
        )
        user.set_password('password')
        user.has_profile_true()
        user.save()
        student = Student(**validated_data)
        student.user = user
        student.save()

        return student


class StudentGroupCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentGroup
        fields = ('student', 'name', 'owner', 'description',)
