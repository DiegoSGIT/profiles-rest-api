from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from profiles_api import serializers, models, permissions

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer
    """ Test APIView """
    def get(self, request, format=None):
        an_apiview = [
            'Esto esta valiendo queso',
            'Dos tripas mijamon',
            'Moronga triposa'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """ Create  Hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'hello ' + name
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        return Response({"message": "Put method"})
    
    def patch(self, request, pk=None):
        return Response({"message": "Path method"})
    
    def delete(self, request, pk=None):
        return Response({"message": "Delete method"})

class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    def list(self, requets):
        an_apiview = [
            'Usess actions (list, create, retrieve, update, partialupdate)',
            'Automatically maps to URLS usgun routes',
            'More functionality without code'
        ]
        return Response({'message': 'Hello!', 'an_viewset': an_apiview})


    def create(self, request):
        """ Create a new create ViewSet """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello ' + name
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        return Response({'http-method': 'GET'})
    
    def update(self, request, pk=None):
        return Response({'http-method': 'PUT'})
        
    def partial_update(self, request, pk=None):
        return Response({'http-method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        return Response({'http-method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    """ This filters allow us to avoid search manually """
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """ Handle creating user authentication tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Viewset to User profile feef """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """ Overwrite the create method by django """         
        serializer.save(user_profile=self.request.user)