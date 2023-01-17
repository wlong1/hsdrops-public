# Run this to create the schedule in the database at first

from django_q.models import Schedule

Schedule.objects.create(func='app.update.tasks.check_drops', minutes=1440, repeats=-1)