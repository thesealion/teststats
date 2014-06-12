from django.db import models


class Hit(models.Model):
    user_id = models.IntegerField()
    page_id = models.IntegerField()
    time = models.DateTimeField()

    def __unicode__(self):
        return 'User: %d, page: %d, %s' % (self.user_id, self.page_id, self.time)
