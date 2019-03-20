from django.shortcuts import render

# Create your views here.

class URLRedirectView(View):

	def get(self, request, shortcode = None, *args, **kwargs):
		obj = get_object_or_404(KirrURL, shortcode = shortcode)
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)
