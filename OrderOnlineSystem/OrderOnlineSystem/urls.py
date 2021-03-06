"""OrderOnlineSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin,auth
from django.urls import path,include
from Login.views import login_view
from django.conf import settings
from django.conf.urls.static import static
# from Login.views import img_show #没写

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Login/',include('Login.urls')),
    path('CustomerSystem/',include('CustomerSystem.urls')),
    path('DispatcherSystem/',include('DispatcherSystem.urls')),
    path('MerchantSystem/',include('MerchantSystem.urls')),
    path('', login_view),
    # path('IMG/',img_show)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)