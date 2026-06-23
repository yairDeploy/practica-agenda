from django.urls import path

from agenda.views.contactoView import ContactoView, inicio
from agenda.views.direccionView import DireccionView
from agenda.views.tabsView import TabsView
from agenda.views.telefonoView import editar_telefonos



urlpatterns = [
    path('', inicio, name='inicio'),
    
    path('crear', ContactoView.crear, name='crear_contacto'),
    path('<int:id>/editar/', ContactoView.editar, name='editar_contacto'),
    path('<int:id>/editar/<str:tab>/', ContactoView.editar, name='editar_contacto'),
    path('<int:id>/eliminar', ContactoView.eliminar, name='eliminar_contacto'),

    path('cargar-tab/<int:id>/<str:tab>/', TabsView.as_view(), name='cargar_tab'),
    path('telefono/<int:contacto_id>/', editar_telefonos, name='editar_telefonos'),

    path('direccion', DireccionView.as_view(), name='direccion'),
]