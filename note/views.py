from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TakeNoteForm, UpdateNoteForm
from .models import Note

    
class IndexView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    template_name = "note/index.html"
    model = Note
    context_object_name = "notes"
    ordering = ["-updated_at"]

class TakeNoteView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')
    template_name = "note/takenote.html"
    form_class = TakeNoteForm

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            note = Note(
                user=request.user, 
                title=form.cleaned_data['title'],
                body=form.cleaned_data['body'],
            )
            note.save()
            return redirect('note:index')
        context = {'form': form}
        return render(request, self.template_name, context)
    

class UpdateNoteView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = UpdateNoteForm
    template_name = "note/updatenote.html"
    success_url = reverse_lazy('note:index')


class DeleteNoteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy("note:index")