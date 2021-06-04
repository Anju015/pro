from django.urls import path
from .import views

urlpatterns = [
        path("emphome",views.home),
        path("pdtreq",views.pdt_req),
]