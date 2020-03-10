import os 
from twilio.rest import Client
def notification_sender(sid,token):
    client = Client(account_sid, auth_token)
    message = client.messages.create(to="+919882746078", from_="+15053369726",body="The following girls have not marked the attendance...")
    return(message.sid) #To print sid
#Your Account SID from twilio.com/console
account_sid ='AC619c5ee6fc583a8e581a8a834fa69266'

 #Your Auth Token from twilio.com/console
auth_token  ='9c264968ca025e433be81db08ff75cb2' #your auth token from twilio console
notification_sender(account_sid,auth_token)