from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views import View

from tickets.models import Ticket

from .forms import QuizForm
from .models import Quiz


class TicketQuizView(View):

    template_name = 'quiz/quiz.html'
    form_class = QuizForm

    def get(self, request, id):
        ticket = get_object_or_404(Ticket, id=id)
        form = self.form_class(questions=ticket.quiz.question_set.all())
        return render(request, self.template_name, {'form': form, 'ticket': ticket})

    def post(self, request, id):
        ticket = get_object_or_404(Ticket, id=id)
        form = self.form_class(ticket.quiz.question_set.all(), request.POST)
        if form.is_valid():
            result = form.cleaned_data['result']
            if result < Quiz.MIN_REQUIRED_RESULT:
                messages.error(request, f'Ваш результат: {result}')
            else:
                messages.success(request, f'Ваш результат: {result}')
            return redirect(reverse('ticket-quiz', args=[id]))
        return render(request, self.template_name, {'form': form, 'ticket': ticket})
