from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404

from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from forum.forms import CommentForm
from forum.models import Comment

from .apps import TicketsConfig
from .models import Ticket


class TicketListView(ListView):
    ''' List all tickets. '''

    model = Ticket
    template_name = f'{TicketsConfig.name}/ticket-list.html'


class TicketDetailView(DetailView):
    ''' Show information about a particular ticket. '''

    model = Ticket
    template_name = f'{TicketsConfig.name}/ticket-detail.html'
    pk_url_kwarg = 'ticket_id'

    def get_context_data(self, **kwargs):
        ''' Return Comments and CommentForm. '''
        context = super().get_context_data(**kwargs)
        context.update({
            'comments': Comment.objects.filter(ticket=self.get_object()),
            'form':     CommentForm(self.get_object(), self.request.user),
        })
        return context


class TicketReadPDFView(View):

    def get(self, request, ticket_filename):
        ticket = get_object_or_404(Ticket, filename=ticket_filename)
        ticket.session_update(request, 'read_tickets')

        try:
            return FileResponse(open(ticket.get_absolute_path(), 'rb'))
        except FileNotFoundError:
            raise Http404
