from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import BoardMessageForm
from .models import BoardMessage, Subject


class BoardMessageCreateView(CreateView): 
    template_name = 'board/create.html'
    form_class = BoardMessageForm 
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subjects"] = Subject.objects.all()
        return context
    

def index(request):
    posts = BoardMessage.objects.order_by('deadline')
    subjects = Subject.objects.all()
    context = {'posts' : posts,
               'subjects' : subjects, }

    return render(request, 'classroom/index.html', context)



def by_subject(request, subject_id): 
    posts = BoardMessage.objects.filter(subject=subject_id)
    subjects = Subject.objects.all()
    current_subject = Subject.objects.get(pk=subject_id)
    
    return render(request,'classroom/by_subject.html', locals() )

