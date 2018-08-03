from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogBlogcategory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=2000)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)
    title_en = models.CharField(max_length=500, blank=True, null=True)
    title_ru = models.CharField(max_length=500, blank=True, null=True)
    title_uk = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_blogcategory'


class BlogBlogpost(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    comments_count = models.IntegerField()
    keywords_string = models.CharField(max_length=500)
    rating_count = models.IntegerField()
    rating_sum = models.IntegerField()
    rating_average = models.FloatField()
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=2000)
    field_meta_title = models.CharField(db_column='_meta_title', max_length=500, blank=True, null=True)  # Field renamed because it started with '_'.
    description = models.TextField()
    gen_description = models.BooleanField()
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    publish_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    short_url = models.CharField(max_length=200, blank=True, null=True)
    in_sitemap = models.BooleanField()
    content = models.TextField()
    allow_comments = models.BooleanField()
    featured_image = models.CharField(max_length=255, blank=True, null=True)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    field_meta_title_en = models.CharField(db_column='_meta_title_en', max_length=500, blank=True, null=True)  # Field renamed because it started with '_'.
    field_meta_title_ru = models.CharField(db_column='_meta_title_ru', max_length=500, blank=True, null=True)  # Field renamed because it started with '_'.
    field_meta_title_uk = models.CharField(db_column='_meta_title_uk', max_length=500, blank=True, null=True)  # Field renamed because it started with '_'.
    content_en = models.TextField(blank=True, null=True)
    content_ru = models.TextField(blank=True, null=True)
    content_uk = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True)
    description_uk = models.TextField(blank=True, null=True)
    title_en = models.CharField(max_length=500, blank=True, null=True)
    title_ru = models.CharField(max_length=500, blank=True, null=True)
    title_uk = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_blogpost'


class BlogBlogpostCategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    blogpost = models.ForeignKey(BlogBlogpost, models.DO_NOTHING)
    blogcategory = models.ForeignKey(BlogBlogcategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_blogpost_categories'
        unique_together = (('blogpost', 'blogcategory'),)


class BlogBlogpostRelatedPosts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    from_blogpost = models.ForeignKey(BlogBlogpost, models.DO_NOTHING)
    to_blogpost = models.ForeignKey(BlogBlogpost, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_blogpost_related_posts'
        unique_together = (('from_blogpost', 'to_blogpost'),)


class ConfSetting(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=2000)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)
    value_en = models.CharField(max_length=2000, blank=True, null=True)
    value_ru = models.CharField(max_length=2000, blank=True, null=True)
    value_uk = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conf_setting'


class CoreSitepermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'core_sitepermission'


class CoreSitepermissionSites(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sitepermission = models.ForeignKey(CoreSitepermission, models.DO_NOTHING)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_sitepermission_sites'
        unique_together = (('sitepermission', 'site'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCommentFlags(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    flag = models.CharField(max_length=30)
    flag_date = models.DateTimeField()
    comment = models.ForeignKey('DjangoComments', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_comment_flags'
        unique_together = (('user', 'comment', 'flag'),)


class DjangoComments(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_pk = models.TextField()
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=254)
    user_url = models.CharField(max_length=200)
    comment = models.TextField()
    ip_address = models.CharField(max_length=39, blank=True, null=True)
    is_public = models.BooleanField()
    is_removed = models.BooleanField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    submit_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_comments'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoRedirect(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)
    old_path = models.CharField(max_length=200)
    new_path = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'django_redirect'
        unique_together = (('site', 'old_path'),)


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    domain = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'django_site'


class FormsField(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    field_order = models.IntegerField(db_column='_order', blank=True, null=True)  # Field renamed because it started with '_'.
    label = models.TextField()
    field_type = models.IntegerField()
    required = models.BooleanField()
    visible = models.BooleanField()
    choices = models.CharField(max_length=1000)
    default = models.CharField(max_length=2000)
    placeholder_text = models.CharField(max_length=100)
    help_text = models.TextField()
    form = models.ForeignKey('FormsForm', models.DO_NOTHING)
    choices_en = models.CharField(max_length=1000, blank=True, null=True)
    choices_ru = models.CharField(max_length=1000, blank=True, null=True)
    choices_uk = models.CharField(max_length=1000, blank=True, null=True)
    default_en = models.CharField(max_length=2000, blank=True, null=True)
    default_ru = models.CharField(max_length=2000, blank=True, null=True)
    default_uk = models.CharField(max_length=2000, blank=True, null=True)
    help_text_en = models.TextField(blank=True, null=True)
    help_text_ru = models.TextField(blank=True, null=True)
    help_text_uk = models.TextField(blank=True, null=True)
    label_en = models.TextField(blank=True, null=True)
    label_ru = models.TextField(blank=True, null=True)
    label_uk = models.TextField(blank=True, null=True)
    placeholder_text_en = models.CharField(max_length=100, blank=True, null=True)
    placeholder_text_ru = models.CharField(max_length=100, blank=True, null=True)
    placeholder_text_uk = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forms_field'


class FormsFieldentry(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    field_id = models.IntegerField()
    value = models.CharField(max_length=2000, blank=True, null=True)
    entry = models.ForeignKey('FormsFormentry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'forms_fieldentry'


class FormsForm(models.Model):
    page_ptr = models.ForeignKey('PagesPage', models.DO_NOTHING, primary_key=True)
    content = models.TextField()
    button_text = models.CharField(max_length=50)
    response = models.TextField()
    send_email = models.BooleanField()
    email_from = models.CharField(max_length=254)
    email_copies = models.CharField(max_length=200)
    email_subject = models.CharField(max_length=200)
    email_message = models.TextField()
    button_text_en = models.CharField(max_length=50, blank=True, null=True)
    button_text_ru = models.CharField(max_length=50, blank=True, null=True)
    button_text_uk = models.CharField(max_length=50, blank=True, null=True)
    content_en = models.TextField(blank=True, null=True)
    content_ru = models.TextField(blank=True, null=True)
    content_uk = models.TextField(blank=True, null=True)
    email_message_en = models.TextField(blank=True, null=True)
    email_message_ru = models.TextField(blank=True, null=True)
    email_message_uk = models.TextField(blank=True, null=True)
    email_subject_en = models.CharField(max_length=200, blank=True, null=True)
    email_subject_ru = models.CharField(max_length=200, blank=True, null=True)
    email_subject_uk = models.CharField(max_length=200, blank=True, null=True)
    response_en = models.TextField(blank=True, null=True)
    response_ru = models.TextField(blank=True, null=True)
    response_uk = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forms_form'


class FormsFormentry(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    entry_time = models.DateTimeField()
    form = models.ForeignKey(FormsForm, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'forms_formentry'


class GalleriesGallery(models.Model):
    page_ptr = models.ForeignKey('PagesPage', models.DO_NOTHING, primary_key=True)
    content = models.TextField()
    zip_import = models.CharField(max_length=100)
    content_en = models.TextField(blank=True, null=True)
    content_ru = models.TextField(blank=True, null=True)
    content_uk = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'galleries_gallery'


class GalleriesGalleryimage(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    field_order = models.IntegerField(db_column='_order', blank=True, null=True)  # Field renamed because it started with '_'.
    file = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    gallery = models.ForeignKey(GalleriesGallery, models.DO_NOTHING)
    description_en = models.CharField(max_length=1000, blank=True, null=True)
    description_ru = models.CharField(max_length=1000, blank=True, null=True)
    description_uk = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'galleries_galleryimage'


class GenericAssignedkeyword(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_pk = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    keyword = models.ForeignKey('GenericKeyword', models.DO_NOTHING)
    field_order = models.IntegerField(db_column='_order', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'generic_assignedkeyword'


class GenericKeyword(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=500)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)
    slug = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'generic_keyword'


class GenericRating(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    value = models.IntegerField()
    rating_date = models.DateTimeField(blank=True, null=True)
    object_pk = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'generic_rating'


class GenericThreadedcomment(models.Model):
    comment_ptr = models.ForeignKey(DjangoComments, models.DO_NOTHING, primary_key=True)
    rating_count = models.IntegerField()
    rating_sum = models.IntegerField()
    rating_average = models.FloatField()
    by_author = models.BooleanField()
    replied_to = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'generic_threadedcomment'


class PagesLink(models.Model):
    page_ptr = models.ForeignKey('PagesPage', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'pages_link'


class PagesPage(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    keywords_string = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=2000)
    field_meta_title = models.CharField(db_column='_meta_title', max_length=500, blank=True, null=True)  # Field renamed because it started with '_'.
    description = models.TextField()
    gen_description = models.BooleanField()
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    publish_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    short_url = models.CharField(max_length=200, blank=True, null=True)
    in_sitemap = models.BooleanField()
    field_order = models.IntegerField(db_column='_order', blank=True, null=True)  # Field renamed because it started with '_'.
    in_menus = models.CharField(max_length=100, blank=True, null=True)
    titles = models.CharField(max_length=1000, blank=True, null=True)
    content_model = models.CharField(max_length=50, blank=True, null=True)
    login_required = models.BooleanField()
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)
    field_meta_title_en = models.CharField(db_column='_meta_title_en', max_length=500, blank=True, null=True)  # Field renamed because it started with '_'.
    field_meta_title_ru = models.CharField(db_column='_meta_title_ru', max_length=500, blank=True, null=True)  # Field renamed because it started with '_'.
    field_meta_title_uk = models.CharField(db_column='_meta_title_uk', max_length=500, blank=True, null=True)  # Field renamed because it started with '_'.
    description_en = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True)
    description_uk = models.TextField(blank=True, null=True)
    title_en = models.CharField(max_length=500, blank=True, null=True)
    title_ru = models.CharField(max_length=500, blank=True, null=True)
    title_uk = models.CharField(max_length=500, blank=True, null=True)
    titles_en = models.CharField(max_length=1000, blank=True, null=True)
    titles_ru = models.CharField(max_length=1000, blank=True, null=True)
    titles_uk = models.CharField(max_length=1000, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages_page'


class PagesRichtextpage(models.Model):
    page_ptr = models.ForeignKey(PagesPage, models.DO_NOTHING, primary_key=True)
    content = models.TextField()
    content_en = models.TextField(blank=True, null=True)
    content_ru = models.TextField(blank=True, null=True)
    content_uk = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages_richtextpage'


class TwitterQuery(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    type = models.CharField(max_length=10)
    value = models.CharField(max_length=140)
    interested = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'twitter_query'


class TwitterTweet(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    remote_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    profile_image_url = models.CharField(max_length=200, blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    retweeter_profile_image_url = models.CharField(max_length=200, blank=True, null=True)
    retweeter_user_name = models.CharField(max_length=100, blank=True, null=True)
    retweeter_full_name = models.CharField(max_length=100, blank=True, null=True)
    query = models.ForeignKey(TwitterQuery, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'twitter_tweet'
