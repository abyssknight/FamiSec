from django.db import models

class Member(models.Model):
  name = models.CharField(max_length=200)
  alias = models.CharField(max_length=200)
  email_address = models.EmailField(max_length=200)
  
  MEMBER_STATUSES = (
      ('A', 'Active'),
      ('I', 'Inactive'),
  )
  
  status = models.CharField(max_length=1, choices=MEMBER_STATUSES, default='A')
  last_modified = models.DateTimeField(auto_now=True, auto_now_add=True)

  def __unicode__(self):
    return u'%s (%s)' % (self.name, self.alias)

class Badge(models.Model):
  card_id = models.CharField(max_length=50, unique=True)
  owner = models.ForeignKey(Member)
  last_modified = models.DateTimeField(auto_now=True, auto_now_add=True)

  def __unicode__(self):
    return u'%s' % (self.card_id)

class BadgeLog(models.Model):
  card = models.ForeignKey(Badge, blank=False, null=False, to_field='card_id')
  owner = models.ForeignKey(Member, blank=False, null=False)
  login_date = models.DateTimeField(auto_now=True, auto_now_add=True)
