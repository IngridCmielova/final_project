from django.urls import path
from . import views


urlpatterns = [
    path('price_list', views.PriceListView.as_view(), name='price_list'),
    path('reservation', views.date_procedure_selection_view, name='reservation'),
    path('schedule/<str:date>/<int:procedure_id>/', views.day_schedule_view, name='day_schedule'),
    path('my_reservations', views.my_reservations_view, name='my_reservations'),
    path('delete_reservation/<int:pk>/', views.delete_reservation_view, name='delete_reservation')
]
