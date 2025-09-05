from .config import settings
from celery import Celery

celery_app = Celery(
    "Quantifyre",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    # include=["src.services.email.service", "src.services.forex.service"],
    # include=["tasks.email_tasks", "tasks.forex_tasks"]
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    enable_utc=True,
    timezone=settings.TIMEZONE,
    task_track_started=True,
    broker_connection_retry_on_startup=True,
    broker_transport_options={
        "max_connections": 32,  # This is the correct way for Redis
        "health_check_interval": 30,
    },
)


# Dispatcher runs every minute to check schedules
celery_app.conf.beat_schedule = {
    "timezone-dispatcher": {
        "task": "app.tasks.timezone_dispatcher",
        "schedule": 60.0,  # Every 60 seconds
    }
}

# Option 2: Autodiscover from all feature folders
celery_app.autodiscover_tasks(
    ["src.auth", "src.user", "src.payment", "src.account", "src.trading"]
)
