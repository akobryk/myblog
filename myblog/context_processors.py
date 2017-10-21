from .settings import PORTAL_URL

def blog_proc(request):
	return {'PORTAL_URL': PORTAL_URL}

