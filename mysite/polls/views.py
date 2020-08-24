from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import F

from .models import Features, ProductArea, Client

class IndexView(generic.ListView):
    models = Features
    template_name = 'polls/index.html'
    context_object_name = 'latest_feature_list'

    def get_queryset(self):
        return Features.objects.all()

class AddFeatureView(generic.ListView):
    model = Client
    template_name = 'polls/addfeature.html'
    
    def get_context_data(self, **kwargs):
        ctx = super(AddFeatureView, self).get_context_data(**kwargs)
        ctx['clients'] = Client.objects.all()
        ctx['areas'] = ProductArea.objects.all()
        ctx['Features'] = map(lambda x: str(x).split(".")[2],   Features._meta.get_fields()[1:] )
        return ctx
        
class SuccessView(generic.ListView):
    model = Client
    template_name = 'polls/success.html'
    context_object_name = 'latest_feature_list'
    
    def get_queryset(self):
        return Features.objects.all()[:5]
    
class ClientListView(generic.ListView):
    model = Client
    context_object_name = 'clientlist'
    
def setfeature(request):
    model = Client
    def get_context_data(self, **kwargs):
        ctx = super(AddFeatureView, self).get_context_data(**kwargs)
        ctx['clients'] = Client.objects.all()
        ctx['areas'] = ProductArea.objects.all()
        ctx['Features'] = map(lambda x: str(x).split(".")[2],   Features._meta.get_fields()[1:] )
        return ctx
       
    sql_fields = list(map(lambda x: str(x).split(".")[2],   Features._meta.get_fields()[1:] ))
    try:
        name_ = request.POST['name']
        description_ = request.POST['description']
        client_ = request.POST['client']
        priority_ = request.POST['priority']
        date_ = request.POST['date']
        area_ = request.POST['parea']
        ct = Client.objects.get(client_text=client_)
        pa = ProductArea.objects.get(prod_area_text=area_)
        f = Features(title = name_, descript = description_, client_type = ct, client_priority = priority_, target_date = date_, product_area = pa)
        
    except:
        # Redisplay the question voting form.
        # return render(request, 'polls/addfeature.html', {
            # 'error_message': "You didn't input correctly.",
        # })
        return HttpResponseRedirect(reverse('polls:addfeature'))   
    else:
        if Features.objects.filter(client_priority = priority_ ):
            entries = Features.objects.filter(client_type = ct)
            entries = entries.filter(client_priority__gte = priority_)
            entries.update(client_priority=F('client_priority') + 1)
        f.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:success'))
