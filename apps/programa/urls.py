from django.urls import path
from .views import programa_detalle, programa_delete, ProgramaCreateView, ProgramaListaView, ProgramaUpdateView

app_name = 'programa'
urlpatterns = [
    # programa views
    path('', ProgramaListaView.as_view(), name='programa_lista'),
    path('<int:pk>/', programa_detalle, name='programa_detalle'),
    path('create/', ProgramaCreateView.as_view(), name='programa_create'),
    path('edit/<int:pk>', ProgramaUpdateView.as_view(), name='programa_edit'),
    path('delete/', programa_delete, name='programa_delete'),
]
