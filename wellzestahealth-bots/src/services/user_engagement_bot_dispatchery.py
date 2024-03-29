from src.models import Model, Organization, User, DotMessage


class UserEngagementDispatcher(Model):
    @classmethod
    def call(klass):
        print('Started User Engagement messages')
        organization = Organization.find()
        for user in User.all():
            if user.score <= 0:
                title = 'Hey {0}: Its been a while. Check out our new events and articles'.format(user.name, user.score)
                DotMessage({
                    'user': user,
                    'organization': organization,
                    'title': title,
                    'subtitle': title,
                    'description': title,
                    'image_url': 'https://cdn.filestackcontent.com/eDG66zx1TIqmpLy9T931'
                }).save()
                print('Message to user id {0} sent!'.format(user.id))
        print('All engagement messages sent')
