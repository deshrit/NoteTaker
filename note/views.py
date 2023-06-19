from typing import Any, Optional

from django.shortcuts import get_object_or_404
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import TakeNoteForm, UpdateNoteForm
from .models import Note
from django.contrib.auth.models import User
from uuid import uuid4

    
class IndexView(ListView):
    template_name = "note/index.html"
    model = Note
    paginate_by = 12
    context_object_name = "notes"

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.user.is_authenticated:
            qs = Note.objects.filter(user=self.request.user).order_by('-updated_at')
            return qs
        
        if self.request.COOKIES.get('guest'):
            qs = Note.objects.filter(user__username=self.request.COOKIES.get('guest')).order_by('-updated_at')
            return qs
        
        qs = Note.objects.none()
        return qs

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        response = super().get(request, *args, **kwargs)
        # assign guest a cookie
        if not request.user.is_authenticated:
            guest = request.COOKIES.get('guest')
            if not guest:
                guest = str(uuid4())
            response.set_cookie(key='guest', value=guest, max_age=8600*10)
            return response
        return response


class TakeNoteView(View):
    template_name = "note/takenote.html"
    form_class = TakeNoteForm

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            
            if request.user.is_authenticated:
                user = request.user
            else:
                guest = request.COOKIES.get('guest')
                if not guest:
                    return redirect('note:index')
                guest_user = User.objects.filter(username=guest).first()
                if not guest_user:
                    guest_user = User(username=guest)
                    guest_user.save()
                    user = guest_user
                user = guest_user

            note = Note(
                user=user,
                title=form.cleaned_data['title'],
                body=form.cleaned_data['body'],
            )
            note.save()
            return redirect('note:index')
        context = {'form': form}
        return render(request, self.template_name, context)
    

class DetailNoteView(DetailView):
    model = Note
    template_name = "note/detailnote.html"
    context_object_name = "note"

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.user.is_authenticated:
            qs = Note.objects.filter(user=self.request.user).order_by('-updated_at')
            return qs
        
        if self.request.COOKIES.get('guest'):
            qs = Note.objects.filter(user__username=self.request.COOKIES.get('guest')).order_by('-updated_at')
            return qs
        
        qs = Note.objects.none()
        return qs
    

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Note, id=pk)
         


class UpdateNoteView(UpdateView):
    model = Note
    form_class = UpdateNoteForm
    template_name = "note/updatenote.html"
    success_url = reverse_lazy('note:index')


class DeleteNoteView(DeleteView):
    model = Note
    success_url = reverse_lazy("note:index")