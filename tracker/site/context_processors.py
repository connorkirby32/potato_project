from google.appengine.api import users
from django.core.urlresolvers import reverse


def general(request):
	return {
		"logout_url": users.create_logout_url(reverse('my-tickets'))
	}
