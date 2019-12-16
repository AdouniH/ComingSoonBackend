

from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import Email
from app1.serialisers import EmailSerializer
from rest_framework import status
from django.views.decorators.clickjacking import xframe_options_exempt


class EmailList(APIView):
    """
    List all Emails
    """

    def get(self, request, format=None):
        emails = Email.objects.all()
        serializer = EmailSerializer(emails, many=True)
        response = Response(serializer.data)
        return response

    def post(self, request, format=None):
        serializer = EmailSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return response
