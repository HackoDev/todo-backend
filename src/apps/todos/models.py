from django.conf import settings
from django.db import models

from django.utils.translation import ugettext_lazy as _


class Task(models.Model):
    QUEUE_STATUS = 0
    LATER_STATUS = 1
    DONE_STATUS = 2
    STATUS_CHOICES = (
        (QUEUE_STATUS, _('In queue')),
        (LATER_STATUS, _('Later')),
        (DONE_STATUS, _('Done')),
    )
    title = models.CharField(_('title'), max_length=512)
    description = models.TextField(_('title'), default='', blank=True)
    due_date = models.DateField(_('due date'))
    status = models.PositiveSmallIntegerField(
        _('status'), choices=STATUS_CHOICES, default=QUEUE_STATUS
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_('user'),
        on_delete=models.CASCADE, related_name='tasks'
    )

    class Meta:
        verbose_name = _('task')
        verbose_name_plural = _('tasks')
