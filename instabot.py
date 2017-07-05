import requests

APP_ACCESS_TOKEN = '3077722633.9208c67.3ee4985723f146bfa542d6872c7fdf8e'
# Token owner : bhagotiarahul
# Sandbox users : instabot , satyansh.snm, harish_rajput70

BASE_URL = 'https://api.instagram.com/v1/'


# getting access to own data

def own_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['following'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'


    # function declaration to get id of a user

def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()


# function declaration to get the details of a user by using username
def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
        request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
        print 'GET request url : %s' % (request_url)
        user_info = requests.get(request_url).json()

        if user_info['meta']['code'] == 200:
                if len(user_info['data']):
                    print 'Username: %s' % (user_info['data']['username'])
                    print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
                    print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
                    print 'No. of posts: %s' % (user_info['data']['counts']['media'])
                else:
                    print 'There is no data for this user!'
        else:
            print 'Status code other than 200 received!'

# menu options of bot

def start_bot():
    while True:
     print '\n'
     print 'Instabot welcomes you'
     print 'choose from following :'
     print "a.Get my details\n"
     print "b.Get details of a user (by username)\n"
     print "j.Exit"

     choice = raw_input("Enter you choice: ")
     if choice == "a":
           own_info()
     elif choice == "b":
         insta_username = raw_input("Enter the username of the user: ")
         get_user_info(insta_username)

     elif choice == "j":
        exit()
    else:
     print "choice doesnt exist"

start_bot()