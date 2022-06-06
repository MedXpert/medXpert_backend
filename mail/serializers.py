from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.core.mail import send_mail


class MailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    body = serializers.CharField()
    to = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
       
        send_mail(
            data['subject'],
            data['body'],
            'medxpert.fall.detection@gmail.com',
            data['to'].split(','),
            fail_silently=False,
        )
        response = {
            'subject': data['subject'],
            'body': data['body'],
            'to': data['to'].split(','),
            'message': 'Email sent successfully'
        }

        return response
