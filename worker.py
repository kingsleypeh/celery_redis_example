from celery import Celery
from celery.utils.log import get_task_logger


# Create the Celery app and get the logger
celery_app = Celery('worker')
celery_app.config_from_object('celeryconfig')
logger = get_task_logger(__name__)


# Do task that adds 2 numbers
@celery_app.task
def add(x, y):
    res = x + y
    logger.info("Adding %s + %s, res: %s" % (x, y, res))
    return res