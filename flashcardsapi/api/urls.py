from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'flashcard', views.FlashCardViewSet)
router.register(r'flashcardset',views.FlashCardSetViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('create/flashcardset/', views.CreateFlashCardSet.as_view(),name="create_flashcard_set"),
    path('create/flashcard/', views.CreateFlashCard.as_view(), name="create_flashcard"),
]
