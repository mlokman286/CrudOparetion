from django.urls import path

from myapp import views


urlpatterns = [
    path('',views.signupPage,name='signupPage'),
    path('loginPage',views.loginPage,name='loginPage'),
    path('homePage',views.homePage,name='homePage'),
    path('addPage',views.addPage,name='addPage'),
    path('editPage',views.editPage,name='editPage'),
    path('updatePage/<str:id>',views.updatePage,name='updatePage'),
]
