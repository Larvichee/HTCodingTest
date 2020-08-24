from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('AddFeature', views.AddFeatureView.as_view(), name='addfeature'),
    path('AddFeature/Set', views.setfeature, name='setfeature'),
    path('AddFeature/Success', views.SuccessView.as_view(), name='success'),
]