import datetime
from src.utils import request
from src.models import Model, User, Organization


class DotMessage(Model):
    QUERY = 'mutation CreateDotMessage($orgId: ID!,  $input: DotMessageInput!) { createDotMessage(organizationId: $orgId, input: $input) { id } }'

    def save(self):
        request(self.QUERY, self._variables())
        return True

    def _variables(self):
        return {
            'orgId': self.organization.id,
            'input': {
                'type': 'IMAGE',
                'title': self.title,
                'subtitle': self.subtitle,
                'description': self.description,
                'publishedOn': self._date(),
                'expiredOn': self._date(),
                'url': self.image_url,
                'scopeType': 'USER',
                'scopeIds': [self.user.id]
            }
        }

    def _date(self):
        return datetime.datetime.today().strftime('%Y-%m-%d')

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        if not isinstance(user, User):
            raise Exception("user must be from User class")
        self._user = user

    @property
    def organization(self):
        return self._organization

    @organization.setter
    def organization(self, organization):
        if not isinstance(organization, Organization):
            raise Exception("organization must be from Organization class")
        self._organization = organization
