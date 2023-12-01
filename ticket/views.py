import random
import string
from django.db import IntegrityError
import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .form import * 
from .models import * 

User = get_user_model()

def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False) # don't save form yet
            var.status = 'Pending'
            var.customer = request.user
            while not var.ticket_id:
                id = ''.join(random.choices(string.digits, k=6))
                try:
                    var.ticket_id = id
                    var.save() # save form in db 
                    # send email to customer 
                    messages.success(request, 'New ticket created and added to the Queue')
                    return redirect('customer-active-tickets')
                except IntegrityError:
                    continue 
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            return redirect('create-ticket')
    else:
        form = CreateTicketForm()
        context = {'form':form}
    return render(request, 'ticket/create_ticket.html', context)

def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    if request.method == 'POST':
        form = UpdateTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ticket information is now updated!') 
            return redirect('customer-active-tickets')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors.')
            # return redirect('update-ticket')
    else:
        form = UpdateTicketForm(instance=ticket)
        context = {'form':form, 'ticket':ticket}
    return render(request, 'ticket/update_ticket.html', context)

def customer_active_tickets(request):
    tickets = Ticket.objects.filter(customer=request.user, is_resolved=False)
    context = {'tickets':tickets}
    return render(request, 'ticket/customer_active_tickets.html', context)

def customer_closed_tickets(request):
    tickets = Ticket.objects.filter(customer=request.user, is_resolved=True)
    context = {'tickets':tickets}
    return render(request, 'ticket/customer_closed_tickets.html', context)

def engineer_active_tickets(request):
    tickets = Ticket.objects.filter(engineer=request.user, is_resolved=False)
    context = {'tickets':tickets}
    return render(request, 'ticket/engineer_active_tickets.html', context)

def engineer_closed_tickets(request):
    tickets = Ticket.objects.filter(engineer=request.user, is_resolved=True)
    context = {'tickets':tickets}
    return render(request, 'ticket/engineer_closed_tickets.html', context)

def unassigned_tickets(request):
    tickets = Ticket.objects.filter(is_assigned=False)
    context = {'tickets':tickets}
    return render(request, 'ticket/unassigned_tickets.html', context)

def assign_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    if request.method == 'POST':
        form = AssignTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_assigned = True
            var.status = 'Active'
            var.date_assigned = datetime.datetime.now()
            var.save()
            messages.success(request, f'Ticket is now assigned to {var.engineer}')
            return redirect('unassigned-tickets')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            #return redirect('assign-ticket')
    else:
        form = AssignTicketForm(instance=ticket)
        form.fields['engineer'].queryset = User.objects.filter(is_engineer=True)
        context = {'form':form}
    return render(request, 'ticket/assign_ticket.html', context)

def resolve_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    if request.method == 'POST':
        ticket.status = 'Closed'
        ticket.is_resolved = True
        ticket.date_closed = datetime.datetime.now()
        ticket.resolution_steps = request.POST.get('rs')
        ticket.save()
        messages.success(request, 'Ticket is now marked as resolved and closed.')
        return redirect('engineer-active-tickets')
    else:
        messages.warning(request, 'Something went wrong. Please, try this action again')
        return redirect('dashboard')
    
def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    context = {'ticket':ticket}
    return render(request, 'ticket/ticket_details.html', context)