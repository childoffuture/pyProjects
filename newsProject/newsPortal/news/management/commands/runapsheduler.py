import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from ...models import CategorySubscribers, Post
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


def news_notify():
    print("----------------------------------------------------------------------------------------------------------------------")

    if CategorySubscribers.objects.all().exists():
        subscribers = CategorySubscribers.objects.all()
        for subscriber in subscribers:
            user = subscriber.id_user
            print(user)
            subject = f'Здравствуй, {user}! Еженедельная рассылка новостей по категории "{subscriber.id_category}"'

            postList = Post.objects.filter(created__gte=(datetime.today() - timedelta(days=7)), id_post_category=subscriber.id_category.pk)
            for post in postList:
                print(post.header, post.created, subscriber.id_category)

            html_content = render_to_string('distribution.html', {'postList': postList, })
            msg = EmailMultiAlternatives(
                subject=subject,
                body='',
                from_email='pyataevfamily@yandex.ru',
                to=[user.email],
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send() # Сообщения могут не приходить, тк яндекс иногда блокирует ящик, считая что идет спам-рассылка(((


def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            news_notify,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            #trigger=CronTrigger(second="*/30"),
            id="news_notify",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'news_notify'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")

