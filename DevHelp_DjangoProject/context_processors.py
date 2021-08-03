from settings.models import Site


def get_site_settings(request):
    return {'site': Site.objects.last()}
