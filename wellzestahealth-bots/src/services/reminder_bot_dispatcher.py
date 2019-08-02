from src.models import Model, User, Organization, DotMessage

class ReminderBotDispatcher(Model):
    @classmethod
    def call(klass):
        print('Started Reminder messages')
        organization = Organization.find()
        for user in User.all():
            title = 'Hey, remember to do something {0}!'.format(user.name)
            DotMessage({
                'user': user,
                'organization': organization,
                'title': title,
                'subtitle': title,
                'description': title,
                'image_url': ''
            }).save()
        print('All Reminder messages sent')