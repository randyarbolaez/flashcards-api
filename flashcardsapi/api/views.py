from django.shortcuts import render
from rest_framework import viewsets,generics

from .serializers import FlashCardSerializer,FlashCardSetSerializer
from .models import FlashCard,FlashCardSet

# Create your views here.

class CreateFlashCard(generics.CreateAPIView):
    '''
    API TO CREATE INDIVIDUAL FLASHCARD
    '''
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer

class CreateFlashCardSet(generics.CreateAPIView):
    '''
    API TO CREATE FLASHCARD SET
    '''
    queryset = FlashCardSet.objects.all()
    serializer_class = FlashCardSetSerializer

class FlashCardViewSet(viewsets.ModelViewSet):
    '''
    API ENDPOINT THAT ALLOWS SPECIFIC FLASHCARD TO BE VIEWED
    '''
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer

class FlashCardSetViewSet(viewsets.ModelViewSet):
    '''
    API ENDPOINT THAT ALLOWS FLASHCARD SETS TO BE VIEWS
    '''
    queryset = FlashCardSet.objects.all()
    serializer_class = FlashCardSetSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)







