from django.urls import path
from .views import programa_lista, programa_detalle, programa_create, programa_edit, programa_delete


app_name = 'programa'
urlpatterns = [
    # programa views
    path('', programa_lista, name='programa_lista'),
    path('<slug:slug>/', programa_detalle, name='programa_detalle'),
    path('create/', programa_create, name='programa_create'),
    path('edit/<int:pk>', programa_edit, name='programa_edit'),
    path('delete/', programa_delete, name='programa_delete'),
]
