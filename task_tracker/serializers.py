from rest_framework import serializers
from task_tracker.models import Task, Status


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'


class TaskSerialezer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
