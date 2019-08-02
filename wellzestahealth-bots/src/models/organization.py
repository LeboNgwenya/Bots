from src.utils import request
from src.models import Model


class Organization(Model):
    QUERY = 'query GetOrganization { accessToken { organization { id } } }'  # noqa: ignore=E501

    @classmethod
    def find(klass):
        data = request(Organization.QUERY, None)
        return Organization({'id': data['data']['accessToken']['organization']['id']})

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if not id:
            raise Exception("id cannot be empry")
        self._id = id
