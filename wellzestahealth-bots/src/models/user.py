from src.utils import request
from src.models import Model


class User(Model):
    QUERY = 'query GetCurrentMonthScore($cursor: String) { accessToken { organization { id users(first: 50, after: $cursor) { edges { node { id fullName birthday currentMonthScore(organizationId: "id" ) } } pageInfo { endCursor hasNextPage } } } } }'  # noqa: ignore=E501

    @classmethod
    def all(klass):
        users = []
        has_next_page = True
        end_cursor = None
        while has_next_page:
            data = request(User.QUERY, {'cursor': end_cursor})
            raw_users = data['data']['accessToken']['organization']['users']['edges']
            users += list(map(lambda x: User({'id': x['node']['id'], 'score': x['node']['currentMonthScore'], 'name': x['node']['fullName'], 'birthday': x['node']['birthday']}), raw_users))
            has_next_page = data['data']['accessToken']['organization']['users']['pageInfo']['hasNextPage']
            end_cursor = data['data']['accessToken']['organization']['users']['pageInfo']['endCursor']
        return users

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if not id:
            raise Exception("id cannot be empry")
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise Exception("name cannot be empty")
        self._name = name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score or 0
