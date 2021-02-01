from rest_framework import serializers
from .models import FlashCard,FlashCardSet

class FlashCardSetSerializer(serializers.HyperlinkedModelSerializer):
    flashcards = serializers.SerializerMethodField()

    class Meta:
        model= FlashCardSet
        fields = ['title','flashcards']

    def get_flashcards(self, obj):
        flashcardset = []
        for i in FlashCard.objects.all():
            if(i.flashcardset == obj):
                flashcardset.append({'question':i.question,'answer':i.answer})

        return flashcardset

class FlashCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FlashCard
        fields = ['question','answer','flashcardset']
