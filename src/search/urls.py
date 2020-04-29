from django.urls import path,re_path
from search.views import (
        SearchProductView,
    )

app_name='search'
urlpatterns = [
    path('',SearchProductView.as_view(),name='query'),
]