from django.shortcuts import render
from .models import Imagen
from .models import ImageForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    lista_imagenes = Imagen.objects.all()
    context = {'lista_imagenes' : lista_imagenes}
    return render(request, 'polls/index.html', context)


def add_image(request):
    if request.method=='POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print 'Se guardo'

            return HttpResponseRedirect(reverse('images:index'))

    else:
        form = ImageForm()
        print 'No se guardo'

    return render(request, 'polls/image_form.html', {'form':form})
