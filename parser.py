import sys, feedparser,pynotify,email

newEmail=""

txt=open("password.txt")
user=txt.readline()
user=str(user)
user=user[:-1]



USERNAME=user
password=txt.readline()
password=str(password)
password=password[:-1]
PASSWORD=password

#print PASSWORD


PROTO="https://"
SERVER="mail.google.com"
PATH="/gmail/feed/atom"
#We assign variables with values. Fill in your username and password
def mail(checker):
    email = int(feedparser.parse(
        PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH
    )["feed"]["fullcount"])

    if email > 0:
        #message = email.message_from_bytes(text) 
        #print (message['Subject'])
        #print "new message arrived"
        
        pynotify.init("Test")
        notice = pynotify.Notification("New mail arrived")
        
        print notice
        
        
        
        
        
        notice.show()
        #notice1.show()
    else:
        newEmail = 0
    

    
         

