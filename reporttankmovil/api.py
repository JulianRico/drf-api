from .models import ReportTankMovil
from rest_framework import viewsets, permissions
from .serializers import ReportSerializer
from .permissions import IsAuthenticatedByJWT


class ReportViewSet(viewsets.ModelViewSet):
    queryset = ReportTankMovil.objects.all()
    permission_classes = [IsAuthenticatedByJWT]
    serializer_class = ReportSerializer