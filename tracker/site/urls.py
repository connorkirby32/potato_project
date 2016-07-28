from django.conf.urls import url, patterns

from .views import (
	my_tickets_view,
	create_project_view,
	update_project_view,
	project_view,
	create_ticket_view,
	update_ticket_view,
	project_list_view,
	update_project_view
)


urlpatterns = patterns(
    '',
    url(r'^projects/$', project_list_view, name='project-list'),
    url(r'^projects/create/$', create_project_view, name='project-create'),
    url(
    	r'^projects/(?P<project_id>\d+)/tickets/create$',
    	create_ticket_view,
    	name='ticket-create'
	),
    url(
    	r'^projects/(?P<project_id>\d+)/tickets/(?P<ticket_id>\d+)/edit$',
    	update_ticket_view,
    	name='ticket-update'
	),
    url(
    	r'^projects/(?P<project_id>\d+)/edit/$',
    	update_project_view,
    	name='project-update'
	),
    url(
    	r'^projects/(?P<project_id>\d+)/$', project_view, name='project-detail'),
    url(r'^$', my_tickets_view, name='my-tickets'),
)
