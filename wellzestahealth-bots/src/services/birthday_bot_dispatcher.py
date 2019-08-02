import datetime
from src.models import Model, User, Organization, DotMessage


class BirthdayBotDispatcher(Model):
    @classmethod
    def call(klass):
        print('Started birthday messages')
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        organization = Organization.find()
        for user in User.all():
            if user.birthday == today:
                title = 'Happy birthday {0}!'.format(user.name)
                DotMessage({
                    'user': user,
                    'organization': organization,
                    'title': title,
                    'subtitle': title,
                    'description': title,
                    'image_url': 'https://cdn.filestackcontent.com/SdMWlmneRyiQBCxG4KUw'
                }).save()
        print('All birthday messages sent')
