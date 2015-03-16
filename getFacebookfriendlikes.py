import requests # pip install requests
import json
import facebook

#Fill your Access token
#Get it from here https://developers.facebook.com/tools/explorer/
ACCESS_TOKEN = ''

g = facebook.GraphAPI(ACCESS_TOKEN)

# Get friends 
friends = g.get_connections("me", "friends")

# Append a file
f=open("result", "ab")

# Loop All friend
while(friends['data']):
    try:
	for friend in friends['data']:
	    # Use list to record friend and like info
	    list=[]
	    friendinfo={'friendid':friend['id'],'friendname':friend['name']}
	    list.append(friendinfo)
#For test
#	    print friend['name']

	    # Get friend's like
	    likes = g.get_connections(friend['id'], "likes")
	    pagecount=0
	    while(likes['data']):
		    try:
			# If friend's likes too many , break it.
		        pagecount=pagecount+1
#For test
#			print pagecount
			if(pagecount==11):
			  break
			# Loop the friend's likes
			for likedata in likes['data']:
			    friendlike={'category':likedata['category'],'name':likedata['name'],'id':likedata['id']}
			    list.append(friendlike)
#For test
#			    print likedata['name']
#		        print likes
		        #print "Next Page:"
		        #print likes['paging']['next']
			# Get friend's like next page,default 25
		        likes=requests.get(likes['paging']['next']).json()
		    except  KeyError:
			break
	    # dump reult to JSON and to a file
	    likejson=json.dumps(list)
	    print likejson
	    f.write(likejson)
	    f.write("\n")
#for test
        #print likes
        #print "Next Page:"
        #print likes['paging']['next']

	# Get friends next page, default 25
	friends=requests.get(friends['paging']['next']).json()
    except  KeyError:
	break
#close file
f.close()
