from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['lancen:index', 'lancen:courses_list', 'lancen:contact', 'lancen:stock']

    def location(self, item):
        return reverse(item)