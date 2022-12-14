from rest_framework import serializers
from user.models import User, Student, Teacher, Admin, StudentGroup, StudentBulkUpload
from rest_framework.validators import UniqueValidator


class StudentBulkCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentBulkUpload
        fields = ['csv_file',]



class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class StudentGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ('name', 'owner', 'description', 'student', )

class StudentGroupListSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(label='id', read_only = True)
    class Meta:
        model = StudentGroup
        fields = '__all__'


class StudentCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', validators =[UniqueValidator(queryset=User.objects.all())] )
    password = serializers.CharField(write_only = True, source='user.password')
    gender = serializers.CharField(source = 'user.gender')
    birthday = serializers.DateField(source = 'user.birthday')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    father_name = serializers.CharField(source = 'user.father_name')
    email = serializers.CharField(source = 'user.email')
    phone = serializers.CharField(source = 'user.phone')
    studentgroups = serializers.PrimaryKeyRelatedField(queryset=StudentGroup.objects.all(), many=True, write_only=True,)
    class Meta:
        model = Student
        fields = ('username', 'password', 'gender', 'birthday', 'first_name', 'last_name', 'email', 'phone', 'education_start_date', 'studentgroups',
        'father_name',)

    def create(self, validated_data):

        user = validated_data.pop('user')
        users = User.objects.create(**user)
        users.set_password(user['password'])
        users.has_profile_true()
        users.save()

        groups = validated_data.pop('studentgroups', [])
        student = Student(**validated_data)
        student.user = users
        student.save()

        for obj in groups:
            obj.student.add(student.id)

        return student


    def update(self, instance, validated_data):
        user = validated_data.pop('user')
        new_groups = validated_data.pop('studentgroups', [])
        #for User Update
        for attr, value in user.items():
            setattr(instance.user, attr, value)
        if user.get('password'):
            instance.user.set_password(user['password'])
        #for Student Update
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.user.save()
        instance.save()
        return instance


class StudentListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Student
        fields = '__all__'

    def get_user(self, obj):
        id = obj.user
        serializer_userId = UserListSerializers(id, many=False)

        return serializer_userId.data

class StudentGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ('name', 'owner', 'description', 'student',)

class StudentGroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = '__all__'

class TeacherCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(write_only = True, source='user.password')
    gender = serializers.CharField(source = 'user.gender')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    email = serializers.CharField(source = 'user.email')
    phone = serializers.CharField(source = 'user.phone')
    birthday = serializers.DateField(source = 'user.birthday')
    father_name = serializers.CharField(source = 'user.father_name')
    class Meta:
        model = Teacher
        fields = ('username', 'password', 'gender', 'birthday', 'first_name', 'last_name', 'email', 'phone', 'position', 'father_name')

    def create(self, validated_data):
        user = validated_data.pop('user')
        users = User.objects.create(**user)

        users.set_password(user['password'])
        users.has_profile_true()
        users.save()

        teacher = Teacher(**validated_data)
        
        teacher.user = users
        teacher.save()

        return teacher

    def update(self, instance, validated_data):
        user = validated_data.pop('user')
        #for User Update
        for attr, value in user.items():
            setattr(instance.user, attr, value)
        if user.get('password'):
            instance.user.set_password(user['password'])
        #for Student Update
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.user.save()
        instance.save()

        return instance


class AdminCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(write_only = True, source='user.password')
    gender = serializers.CharField(source = 'user.gender')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    email = serializers.CharField(source = 'user.email')
    phone = serializers.CharField(source = 'user.phone')
    birthday = serializers.DateField(source = 'user.birthday')
    father_name = serializers.CharField(source = 'user.father_name')
    class Meta:
        model = Admin
        fields = ('username', 'password', 'gender', 'birthday', 'first_name', 'last_name', 'email', 'phone', 'father_name')

    def create(self, validated_data):
        user = validated_data.pop('user')
        users = User.objects.create(**user)

        users.set_password(user['password'])
        users.has_profile_true()
        users.save()

        teacher = Teacher(**validated_data)
        
        teacher.user = users
        teacher.save()

        return teacher

    def update(self, instance, validated_data):
        user = validated_data.pop('user')
        #for User Update
        for attr, value in user.items():
            setattr(instance.user, attr, value)
        if user.get('password'):
            instance.user.set_password(user['password'])
        #for Student Update
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.user.save()
        instance.save()

        return instance


class TeacherListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Teacher
        fields = '__all__'
    def get_user(self, obj):
        id = obj.user
        serializer_userId = UserListSerializers(id, many=False)

        return serializer_userId.data