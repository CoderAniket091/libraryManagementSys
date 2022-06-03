from django import views
from django.urls import path
from libsyshome import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('addbooks', views.addbooks, name='signout'),
    path('updatebooks/<int:id>', views.updatebooks, name='updatebook'),
    path('deletebooks/<int:id>', views.deletebooks, name='deletebook'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
