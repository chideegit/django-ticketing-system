from django.urls import path 
from .views import * 

urlpatterns = [
    path('create-ticket/', create_ticket, name='create-ticket'), 
    path('update-ticket/<str:ticket_id>/', update_ticket, name='update-ticket'), 
    path('customer-active-tickets/', customer_active_tickets, name='customer-active-tickets'), 
    path('customer-closed-tickets/', customer_closed_tickets, name='customer-closed-tickets'), 
    path('engineer-active-tickets/', engineer_active_tickets, name='engineer-active-tickets'), 
    path('engineer-closed-tickets/', engineer_closed_tickets, name='engineer-closed-tickets'), 
    path('unassigned-tickets/', unassigned_tickets, name='unassigned-tickets'), 
    path('assign-ticket/<str:ticket_id>/', assign_ticket, name='assign-ticket'), 
    path('resolve-ticket/<str:ticket_id>/', resolve_ticket, name='resolve-ticket'), 
    path('ticket-details/<str:ticket_id>/', ticket_details, name='ticket-details'), 
    path('all-active-tickets/', all_active_tickets, name='all-active-tickets')
]