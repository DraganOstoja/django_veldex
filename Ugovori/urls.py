from django.conf import settings
from django.conf.urls.static import static
from kupoprodaja.views import LandingPageView, landing_page
from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name="landing-page"),
    path('ugovori/', include('kupoprodaja.urls', namespace='kupoprodaja')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)