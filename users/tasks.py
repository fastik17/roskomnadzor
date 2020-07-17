from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.core.mail import send_mail
from django.conf import settings

from sites.models import BlockedSites


@periodic_task(run_every=(crontab(minute='*/10')),
               name="send_email_to_inform_user")
def send_email_to_inform_user():
    blocked_websites = BlockedSites.objects.filter(is_blocked=True, email_was_sent=False)
    for blocked_website in blocked_websites:
        try:
            send_mail(
                subject=f'Your report for "{blocked_website.site.domain_name}".',
                message='ty for reporting.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[blocked_website.site.user_email])
        except Exception as e:
            print(e)
        else:
            blocked_website.email_was_sent = True
            blocked_website.save()
