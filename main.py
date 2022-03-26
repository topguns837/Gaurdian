import os
from socketserver import ThreadingUnixDatagramServer
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

#account_sid = os.environ['AC2bba80a010cef0e584fa20f19e781e3d']
#auth_token = os.environ['2a33059fcad5780294ddfd849ccc204a']


#client = Client('AC2bba80a010cef0e584fa20f19e781e3d', '2a33059fcad5780294ddfd849ccc204a')

'''message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+17208040871',
                     to='+91 9999906505'
                 )'''

#print(message.sid)


class SendMessage():     
        
                 
    def send(self ,sensor , value):

        client = Client('AC2bba80a010cef0e584fa20f19e781e3d', '2a33059fcad5780294ddfd849ccc204a')
        
        message = client.messages \
                .create(
                     body="ALERT ! The " + sensor +" has detected a triggering value of " + str(value),
                     from_='+17208040871',
                     to='+91 9999906505'
                 )
        print(message.sid)