from django.urls import path
from .import views


urlpatterns = [
    path("",views.adminLogin, name=" home page"),

    path("home", views.home, name=" home page"),
    path("classes", views.classes, name="classes page"),
    path("booking", views.booking, name="booking page"),
    path("signup", views.signup, name="signup page"),
    path("login", views.login, name="login page"),

    path("search", views.search, name="search page"),

    path("logout", views.logout, name="logout page"),

    path("dashboard", views.dashboard, name="dashboard page"),

    path("adminlogin", views.adminLogin, name="login page"),
    path("entry", views.entry, name="login page"),

    path("entryCustomer", views.entryCustomer, name="login page"),
    path("showCustomer",views.showCustomer,name="showCustomer page"),

    path("create",views.create,name="Create page"),
    path("show",views.show,name="show page"),
    path("edit/<int:id>",views.edit,name="edit page"),
    path("update/<int:id>",views.update,name="update page"),
    path("delete/<int:id>",views.delete,name="delete page"),
]
