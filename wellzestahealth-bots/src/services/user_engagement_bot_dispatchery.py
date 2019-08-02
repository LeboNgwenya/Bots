from src.models import Model, Organization, User, DotMessage


class UserEngagementDispatcher(Model):
    @classmethod
    def call(klass):
        print('Started User Engagement messages')
        organization = Organization.find()
        for user in User.all():
            if user.score <= 0:
                title = 'Hey {0}: It has been a while since we last saw you at an event'.format(user.name, user.score)
                DotMessage({
                    'user': user,
                    'organization': organization,
                    'title': title,
                    'subtitle': title,
                    'description': title,
                    'image_url': ' '
                }).save()
                print('Message to user id {0} sent!'.format(user.id))
        print('All engagement messages sent')
