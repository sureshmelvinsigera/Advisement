from django.conf.urls import url
from django.urls import path, include
from apps.CSI.views import index_view

urlpatterns = [
    path('', view=index_view, name='student_index_view')
]
