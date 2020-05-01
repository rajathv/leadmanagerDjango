from leads.models import Lead
from rest_framework import viewsets, permissions
from .seraliszers import LeadSeralizer

#lead viewset

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [ permissions.AllowAny]
    serializer_class = LeadSeralizer