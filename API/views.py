from rest_framework import generics, permissions
from .serializers import FeedSerializer,FeedSubscriber,URLSerializers,URLRemoveSerializers
from .models import Feed,SavedURL
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework import status
from django.http import JsonResponse, response
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class FeedList(generics.ListCreateAPIView):
    serializer_class = FeedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return Feed.objects.all().order_by("name")

    def perform_create(self, serializer):
        obj = serializer.save()
        obj.Users.add(self.request.user)

class UserFeedList(generics.ListAPIView):
    serializer_class = FeedSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Feed.objects.filter(Users = self.request.user).order_by("name")


class CategoryFeedList(generics.ListAPIView):
    serializer_class = FeedSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        Category = self.kwargs['category']
        if(not Category):
            Category = "General"
        return Feed.objects.filter(Category__icontains = Category).order_by("name")

class FeedSubscribe(generics.UpdateAPIView):
    serializer_class = FeedSubscriber
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Feed.objects.all()

    def perform_update(self, serializer):
        serializer.instance.Users.add(self.request.user)
        serializer.save()


class FeedUnSubscribe(generics.UpdateAPIView):
    serializer_class = FeedSubscriber
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Feed.objects.all()

    def perform_update(self, serializer):
        serializer.instance.Users.remove(self.request.user)
        serializer.save()


class SavedRemove(generics.UpdateAPIView):
    serializer_class = URLRemoveSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SavedURL.objects.all()

    def perform_update(self, serializer):
        serializer.instance.Users.remove(self.request.user)
        serializer.save()

class SaveURL(generics.ListCreateAPIView):
    serializer_class = URLSerializers
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return SavedURL.objects.filter(Users = self.request.user)
    def perform_create(self, serializer):
        data = self.request.data
        temp = SavedURL.objects.filter(url = data['url']) 
        ttl = temp.filter(Users = self.request.user)
        if not temp:
            obj = serializer.save()
            obj.Users.add(self.request.user)
        else :
            if not ttl:
                for t in temp:
                    t.Users.add(self.request.user)
            else:
                raise ParseError(detail="Saved Duplication")



        
        


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(data['username'], password=data['password'], email = data['email'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({'error':'That username has already been taken. Please choose a new username'}, status=400)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'], email = data['email'])
        if user is None:
            return JsonResponse({'error':'Could not login. Please check username and password'}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=200)

