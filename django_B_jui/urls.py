from django.urls import include, path
#from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_B_jui.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    path('', include('bui_app.urls')),
]
