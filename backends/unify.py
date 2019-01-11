from social_core.backends.oauth import BaseOAuth2
from django.conf import settings

class UnifyOAuth2(BaseOAuth2):
    """Taobao OAuth authentication mechanism"""
    name = 'unify'
    ID_KEY = 'username'  #<===== SET THIS TO UNIQUE ATTRIBUTE IF ID IS NOT RETURNED
    ACCESS_TOKEN_METHOD = 'POST'
    AUTHORIZATION_URL = '%so/authorize' % settings.SOCIAL_AUTH_UNIFY_DOMAIN
    REQUEST_TOKEN_URL = '%so/request_token' % settings.SOCIAL_AUTH_UNIFY_DOMAIN
    ACCESS_TOKEN_URL = '%so/token/' % settings.SOCIAL_AUTH_UNIFY_DOMAIN
    PROFILE_URL = '%saccounts/fullprofiles/0/' % settings.SOCIAL_AUTH_UNIFY_DOMAIN

    def get_user_details(self, response):
        print ("user detail: ", response)
        """Return user details from GitHub account"""
        return {'username': response.get('username'),
                'email': response.get('email', ''),
                'fullname': response.get('truename')}

    def user_data(self, access_token, *args, **kwargs):
        """Return user data provided"""
        return self.get_json(
            self.PROFILE_URL,
            headers={'Authorization': 'Bearer {0}'.format(access_token)}
        )


'''
http://unify.91dbq.com:8000/o/authorize?
response_type=code
&state=random_state_string&client_id=DoNPsvD1IP1WbcBIYddkSiAeonzhy5KLcL7dtNFf

http://unify.91dbq.com:8000/o/authorize?
state=KI2ITW0uWnfUX8j2lISsm5ldngSOq2vI&
redirect_uri=http%3A%2F%2F127.0.0.1%3A8001%2Fcomplete%2Fjfpal%2F%3Fredirect_state%3DKI2ITW0uWnfUX8j2lISsm5ldngSOq2vI&
response_type=code
&client_id=None

'''