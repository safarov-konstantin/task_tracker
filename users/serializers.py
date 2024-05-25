from rest_framework import serializers
from users.models import User, Position
from task_tracker.serializers import TaskSerialezer


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'phone',
            'position',
            'tasks',
            'password',
        ]

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        new_user = User(**validated_data)
        new_user.set_password(password)
        new_user.is_staff = False
        new_user.is_active = True
        new_user.save()
        return new_user


class EmployedUserSerializer(serializers.ModelSerializer):

    tasks = TaskSerialezer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'phone',
            'position',
            'tasks',
        ]


class AvailableUserForTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'phone',
            'position',
            'tasks',
        ]
