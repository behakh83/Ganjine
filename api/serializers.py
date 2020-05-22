from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Collection, Question


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'grade', 'name']


class CollectionSerializerDetail(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'grade', 'name', 'question_set']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'collection', 'question_text', 'option1', 'option2',
                  'option3', 'option4', 'correct_option', 'date_update']
