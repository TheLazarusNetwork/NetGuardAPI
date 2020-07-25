from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.




class CreateNewGuardView(APIView):
    api_view=['POST',]

    def post(self, request):
        return Response("success", status.HTTP_200_OK)

class GetNetGuardView(APIView):
    api_view=['GET',]

    def get(self, request):
        return Response("success", status.HTTP_200_OK)