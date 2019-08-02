from src.models import Model, Organization, User, DotMessage


class PointsBotDispatcher(Model):
    @classmethod
    def call(klass):
        print('Started sending points messages')
        organization = Organization.find()
        for user in User.all():
            if user.score >= 50:
                title = 'Congratulations {0}: you reached {1} points'.format(user.name, user.score)
                DotMessage({
                    'user': user,
                    'organization': organization,
                    'title': title,
                    'subtitle': title,
                    'description': title,
                    'image_url': 'https://cdn.filestackcontent.com/CIoVq6dbRPGdY4p2aFsA'
                }).save()
                print('Message to user id {0} sent!'.format(user.id))
        print('All points messages sent')
