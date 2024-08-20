import datetime

from livekit import api


class TokenGenerator:
    def __init__(self, room_name):
        super(TokenGenerator, self).__init__()
        self.room_name = room_name

    def create_token(self, pk):
        token = api.AccessToken(api_key='APIGzdZGABK3xUN', api_secret='iJFuwTMNJ9lbJkDBonxsINS67fT7kWUy3IpXqyVeenLA') \
            .with_identity(str(pk)) \
            .with_name(str(pk)) \
            .with_ttl(datetime.timedelta(days=1)) \
            .with_grants(api.VideoGrants(
            room_join=True,
            room=self.room_name,
        )).to_jwt()
        return token