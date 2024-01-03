"""
URL configuration for vogue project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authentication import views as authviews
from main import views as mainviews

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', authviews.home),
    path('Signup/', authviews.signup),
    path('Signin/', authviews.signin),
    path('logout/', authviews.logoutuser),

    path('store/', mainviews.store),
    path('product/<int:pd_id>/', mainviews.product, name='product'),
    path('addtocart/<int:pd_id>/', mainviews.add_to_cart, name='addToCart'),
    path('deleteitem/<int:pd_id>/', mainviews.deleteitem, name='delete'),
    path('cart/', mainviews.cart),

    path('checkout/<int:pd_id>/', mainviews.checkout, name='checkout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
