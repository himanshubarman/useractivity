from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta,datetime
from user_activity.models import User, UserActivity
import random
import pytz
import names


#Custom management command  - run by python manage.py generatedata

# for creating dummy data for user and user activity model

class Command(BaseCommand):
    help = 'Generate UserActivity Data'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs.get('count', [20])
        for _ in range(count[0]):
            self.generate_user_data()

    def generate_user_data(self):
        user = User.objects.create(real_name=names.get_full_name(),
                                        tz=random.choice(list(pytz.all_timezones_set)))

        for i in range(3):
            time_delta = timedelta(days=random.randint(1,365))
            start_time = timezone.now() - time_delta
            end_time = start_time + timedelta(minutes=random.randint(5,60))
            activity = UserActivity(start_time=start_time, end_time=end_time, user=user)
            activity.save()