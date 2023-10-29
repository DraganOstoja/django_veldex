from django.urls import path

from report.views import save, edit, run, Index

app_name='report'
urlpatterns = [
    path('reporting/',Index.as_view(),name='reports_page'),
    path('edit/<str:report_type>/', edit, name='report_edit'),
    path('run/', run, name='report_run'),
    path('save/<str:report_type>/', save, name='report_save'),
]
