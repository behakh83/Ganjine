import json

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from api.serializers import UserSerializer, GroupSerializer, CollectionSerializer, QuestionSerializer, \
    CollectionSerializerDetail
from api.models import Collection, Question
from django.http import HttpResponse


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.order_by('grade')
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('grade',)

    def retrieve(self, request, *args, **kwargs):
        queryset = Collection.objects.get(id=kwargs['pk'])
        serializer = CollectionSerializerDetail(queryset, many=False, context={'request': request})
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


@api_view(['GET'])
def test_connection(request):
    return HttpResponse(json.dumps({'status': True}))


@api_view(['GET'])
def about_us(request):
    return HttpResponse(json.dumps({'about_us': 'گنجینه مجموعه ای بی نظیر از بهترین سوالات مطالعات اجتماعی پایه های '
                                                'هفتم، هشتم و نهم است که می تواند شما را برای امتحانات آماده کند.',
                                    'developers': 'برنامه نویس:\n'
                                                  'بهراد آخانی\n'
                                                  'تهیه کنندگان:\n'
                                                  'محمدطاها غفاری\n'
                                                  'محمد رسول خسروی\n'
                                                  'محمد رضا کرمی\n'
                                                  'امیر طاها آقامحمدی\n'}))


@api_view(['GET'])
def collection_count(request):
    seventh = len(Collection.objects.filter(grade=Collection.Grade.SEVENTH))
    eighth = len(Collection.objects.filter(grade=Collection.Grade.EIGHTH))
    ninth = len(Collection.objects.filter(grade=Collection.Grade.NINTH))
    return HttpResponse(json.dumps({'seventh': seventh,
                                    'eighth': eighth,
                                    'ninth': ninth}))

