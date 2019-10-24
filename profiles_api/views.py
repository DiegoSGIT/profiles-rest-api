from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
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