from tkinter import image_names
from django.template import RequestContext
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.shortcuts import redirect, render

from .forms import AddImageForm
from .models import Image

# Create your views here.

class PostListView(ListView):
    model = Image
    template_name = 'images/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'images'
    paginate_by = 9

class PostDetailView(DetailView):
    model = Image
    template_name = 'images/details.html'
    context_object_name = 'image'


def postImage(request):

    if request.method == 'POST':
        form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data.get("imageName"))
            name = form.cleaned_data.get("imageName")
            details = form.cleaned_data.get("imageDetails")
            img = form.cleaned_data.get("imageUrl")
            obj = Image.objects.create(
                                 imageName = name,
                                 imageUrl = img,
                                 imageDetails = details
                                 )
            obj.save()

            return redirect('home')

    else:
        form = AddImageForm()

    return render(request, 'images/image_form.html', {'form' : form})


class PostDeleteView(DeleteView):
    model = Image
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if post:
            return True
        return False


class PostUpdateView(UpdateView):
    model = Image
    fields = ['imageName', 'imageUrl', 'imageDetails']
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post:
            return True
        return False