from django.db import models
from mezzanine.pages.models import Page
from modeltranslation.translator import translator, TranslationOptions
from .models import Author, Book
from modeltranslation.translator import translator
from mezzanine.core.translation import (TranslatedSlugged,
                                        TranslatedDisplayable,
                                        TranslatedRichText)
from mezzanine.blog.models import BlogCategory, BlogPost



class TranslatedBlogPost(TranslatedDisplayable, TranslatedRichText):
    fields = ('title', 'description', 'gen_description')

class TranslatedBlogBlogCategory(TranslatedSlugged):
    fields = ()

translator.register(BlogPost, TranslatedBlogPost)
translator.register(BlogCategory, TranslatedBlogBlogCategory)