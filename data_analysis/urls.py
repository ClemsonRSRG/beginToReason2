"""
This module contains our mapping of URL path expressions to Django views for the "data_analysis" application.
"""
from django.urls import path

from . import views

# URL namespace for this application.
app_name = 'data_analysis'

# URL patterns to be matched.
urlpatterns = [
    path('data/<int:setID>/<int:lessonIndex>', views.d3_graph, name="d3-graph"),
    path('data/<int:setID>', views.set_statistics, name='set-statistics'),
    path('instructor', views.instructor, name='instructor')
]
