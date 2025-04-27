from django.urls import path
from api.views.hello_views import hello_world, hello_name, ai_haiku

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('hello/name/', hello_name, name='hello_name'),
    path('ai/haiku/', ai_haiku, name='ai_haiku'),
] 