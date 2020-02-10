from django.urls import path
from .import views


urlpatterns = [
    path("",views.adminlogin),

    path("home", views.home),
    path("classes", views.classes),
    path("booking", views.booking),
    path("signup", views.signup),
    path("entryCustomer", views.entryCustomer),
    path("showCustomer", views.showCustomer),
    path("login", views.login),
    path("logout", views.logout),
    path("create",views.create),
    path("show",views.show),
    path("edit/<int:id>",views.edit),
    path("update/<int:id>",views.update),
    path("delete/<int:id>",views.delete),

    path("adminlogin", views.adminlogin),
    path("entry", views.entry),
    path("search", views.search),
    path("dashboard", views.dashboard),


]
