from django.db import models


class UserRequest(models.Model):
    domain_name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    user_email = models.EmailField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    additional_info = models.CharField(max_length=254, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = 'Websites Information'
        verbose_name = 'Website Information'

    def __str__(self):
        return self.domain_name


class BlockedSites(models.Model):
    is_blocked = models.BooleanField('Want to block it?', default=False)
    site = models.ForeignKey(UserRequest, on_delete=models.CASCADE)
    email_was_sent = models.BooleanField('User was notified', default=False)

    class Meta:
        verbose_name_plural = 'Blocked Websites'
        verbose_name = 'Blocked Website'
        unique_together = ('is_blocked', 'site')

    def __str__(self):
        return '%s: %s' % (self.id, self.site.domain_name)
