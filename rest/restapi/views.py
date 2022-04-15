from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Categories, Book,Cart
from .serializers import RegistrationSerializer, CategorySerializer, BookSerializer,UserSerializer, CartSerializer
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import permissions
import uuid




class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save()
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)


class CategoryList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated)
    categories =Categories.objects.all()
    serializer_class = CategorySerializer

class BookList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated)
    categories =Book.objects.all()
    serializer_class =BookSerializer

class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListCart(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer 






# action is the indicater of interest
