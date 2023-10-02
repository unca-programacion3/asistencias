from django.urls import path
from .views import persona_lista, persona_create, persona_detalle


app_name = 'persona'
urlpatterns = [
    path('', persona_lista, name='persona_lista'),
    path('<int:pk>/', persona_detalle, name='persona_detalle'),
    path('create/', persona_create, name='persona_create'),
]
