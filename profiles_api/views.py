from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ Test APIView """
    def get(self, request, format=None):
        an_apiview = [
            'Esto esta valiendo queso',
            'Dos tripas mijamon',
            'Moronga triposa'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})