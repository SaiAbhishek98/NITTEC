from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Admin Page.
    path('admin/', admin.site.urls),

    # Home page.
    path('', include('home.urls')),

    # Activities/Communication Logs
    path('Activity-Communication-log/',include('ActComLog.urls')),

    # Amber Alerts.
    path('Amber-Alert/', include('AmberAlert.urls')),

    # Damage claims.
    path('Damage-claims/', include('GeneralEvents.urls')),

    # Equipment Problems.
    path('Equipemnt-problems/', include('GeneralEvents.urls')),

    #General Events.
    path('General-events/', include('GeneralEvents.urls')),

]
