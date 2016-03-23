from django.conf.urls import include, url
from django.contrib import admin
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^state_detail/(?P<name>.+)/$','main.views.state_detail'),
    url(r'^state_list/$','main.views.state_list'),
 #    url(r'^get_post/$','main.views.get_post'),
	# url(r'^get_search/$','main.views.get_search'),
	# url(r'^get_post/$', views.GetPost.as_view()),
	# url(r'^template_view/$','main.views.template_view'),
	url(r'^cbv_detail/(?P<pk>[0-9]+)/$',views.StateDetailView.as_view),
	url(r'^city_search/$', 'main.views.city_search'),  
	url(r'^city_create/$', 'main.views.city_create'),
	url(r'^cbv_edit/(?P<pk>[0-9]+)/$', 'main.views.city_edit'),
	url(r'^cbv_delete/(?P<pk>[0-9]+)/$', 'main.views.city_delete'),

]
