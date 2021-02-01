from django.db import models

# Create your models here.
class FlashCardSet(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class FlashCard(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=100)
    flashcardset = models.ForeignKey(FlashCardSet,on_delete=models.CASCADE)

    def __str__(self):
        return self.question
