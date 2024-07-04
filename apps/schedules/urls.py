from django.urls import path

from .views import TimeListView

urlpatterns = [
    path('time/table/', TimeListView.as_view(), name='time_table')



]