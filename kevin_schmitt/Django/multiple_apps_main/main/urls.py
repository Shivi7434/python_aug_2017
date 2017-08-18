"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include # Notice we added include
from django.contrib import admin
urlpatterns = [
    url(r'^user_login/', include('apps.user_login.urls')),
    url(r'^first_app/', include('apps.first_app.urls')),
    url(r'^blogs', include('apps.blogs.urls')),
    url(r'^sureys/', include('apps.surveys.urls')),
    url(r'^users/', include('apps.users.urls')),
    url(r'^time_display/', include('apps.time_display.urls')),
    url(r'^random_word/', include('apps.random_word.urls')),
    url(r'^admin/', admin.site.urls),
]