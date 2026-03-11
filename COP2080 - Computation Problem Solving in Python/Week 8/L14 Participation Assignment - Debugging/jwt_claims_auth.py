import jwt
import pdb

data = {'payload': 'data', 'iss': 'Headquarters', 'aud': 'learn-python'}
secret = 'secret-key'
token = jwt.encode(data, secret, algorithm="HS256")

def decode(token, secret, issuer=None, audience=None):
    try:
        print(jwt.decode(
            token,
            secret,
            issuer=issuer,
            audience=audience,
            algorithms=["HS256"]
        ))
    except (jwt.InvalidIssuerError, jwt.InvalidAudienceError) as err:
        print(err)
        print(type(err))

pdb.set_trace()
decode(token, secret)
# not providing the issuer won't break
decode(token, secret, audience='learn-python')
# not providing the audience will break
decode(token, secret, issuer='Headquarters')
# both will break
decode(token, secret, issuer='wrong', audience='learn-python')
decode(token, secret, issuer='Headquarters', audience='wrong')
decode(token, secret, issuer='Headquarters', audience='learn-python')