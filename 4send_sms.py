
from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = 'AC9b838a498f68ca855985f13be26b33ce'
AUTH_TOKEN = 'dffb995ca985bec3823e86d12706f517'

# instance of class TwilioRestClient inside twilio.rest module using my credentials
myMessageSender = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

myMessageSender.messages.create(to = '+16504270718', from_ = '+16504828260', body = "Hey hey heyyy")