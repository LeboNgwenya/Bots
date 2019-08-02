from src.models import Model, User, Organization, DotMessage

class PositivityBotDispatcher(Model):
    @classmethod
    def call(klass):
        print('Started Positivity messages')
        organization = Organization.find()
        for user in User.all():
            title = 'Positivity message {0}!'.format(user.name)
            DotMessage({
                'user': user,
                'organization': organization,
                'title': title,
                'subtitle': title,
                'description': title,
                'image_url': 'https://cdn.filestackcontent.com/TUL26wdTRMCsAbz0KGih'
            }).save()
        print('All positivity messages sent')
