from .models import Practice
from rest_framework import viewsets, permissions
from .serializers import PracticeSerializer


class PracticeViewSet(viewsets.ModelViewSet):
    queryset = Practice.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PracticeSerializer
    