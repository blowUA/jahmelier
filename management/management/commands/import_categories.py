from django.core.management.base import BaseCommand
from jahmelier.mezza.models import blo

class Command(BaseCommand):
    def handle(self, *args, **options):
        for c in blog_blogcategory.objects.using('mezza').all():
            print(c.name)
