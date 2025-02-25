from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['index', 'information', 'location', 'direction', 'concierge', 
                'smart', 'premium', 'block', 'dong', 'pyeong', 'apply']

    def location(self, item):
        return reverse(item)
