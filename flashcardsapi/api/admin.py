from django.contrib import admin
from .models import FlashCard,FlashCardSet

# Register your models here.
admin.site.register(FlashCardSet)
admin.site.register(FlashCard)
