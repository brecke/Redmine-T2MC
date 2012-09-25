# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class KbArticles(models.Model):
    id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()
    title = models.CharField(max_length=765)
    summary = models.TextField(blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    author_id = models.IntegerField()
    comments_count = models.IntegerField(null=True, blank=True)
    project_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'kb_articles'

class WikiContents(models.Model):
    id = models.IntegerField(primary_key=True)
    page_id = models.IntegerField()
    author_id = models.IntegerField(null=True, blank=True)
    text = models.TextField(blank=True)
    comments = models.CharField(max_length=765, blank=True)
    updated_on = models.DateTimeField()
    version = models.IntegerField()
    class Meta:
        db_table = u'wiki_contents'

