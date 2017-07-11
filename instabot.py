import requests , urllib

APP_ACCESS_TOKEN = '3077722633.9208c67.3ee4985723f146bfa542d6872c7fdf8e'
# Token owner : bhagotiarahul
# Sandbox users : Vivek3273 , mehulbiswas , Streethustler_1

BASE_URL = 'https://api.instagram.com/v1/'


# function declaration to get access to own data

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

# function declaration to fetch own media

def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            video_name = own_media['data'][0]['id'] + '.mp4'
            video_url = own_media['data'][0]['videos']['standard_resolution']['url']
            urllib.urlretrieve(video_url, video_name)
            print 'video has been downloaded'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'

# function declaration to fetch user's media using username

def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            video_name = user_media['data'][0]['id'] + '.mp4'
            video_url = user_media['data'][0]['videos']['standard_resolution']['url']
            urllib.urlretrieve(video_url,video_name)
            print 'Your video has been downloaded!'
        elif len(user_media['data']):
                image_name = user_media['data'][0]['id'] + '.jpeg'
                image_url = user_media['data'][0]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url, image_name)
                print 'Your image has been downloaded!'
        else:
            print 'post doesnot exist'
    else:
            print 'Status code other than 200 received!'

# function declaration to get ID of recent post of a user

def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'No recent posts found of the user'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()

# function declaration to get like on a user's recent post

def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful'
    else:
        print 'Your like was unsuccessful. Try again!'

# function declaration to add comment on a user's recent post

def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("add your comment: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "your comment was added"
    else:
        print "No comments could be added , please try again."

# function declaration of list of likes made by user on post

def get_like_list(insta_username):
    media_id=get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    print 'GET request url : %s' % (request_url)
    like_list = requests.post(request_url).json()

    if like_list['meta']['code'] == 200:
        print like_list
    else:
        print 'status code other than 200 received'

# function declaration of list of comments made on users post

def get_comment_list(media_id):
    list_of_comments = get_comment_list(media_id)
    if list_of_comments== None:
        print 'no media exists'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (list_of_comments, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_list = requests.get(request_url).json()

    if comment_list['meta']['code'] == 200:
        if len(comment_list['data']):
            print 'list of comments : %s'%(comment_list['data'][0]['id'])
        else:
            print 'post has no comments '
    else:
        print 'status code other than 200 received'

    if comment_list['meta']['code'] == 200:
        print comment_list
    else:
        print 'status code other than 200 received'

# function declaration for trending post

def get_trending post(media_id):
    list_of_comments = get_comment_list(media_id)
    list_of_likes = get_like_list(media_id)
    if list_of_likes== None:
        print 'no trending post found'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (list_of_likes,APP_ACCESS_TOKEN)
    print 'GET request url : &s' % (request_url)
    like_list = requests.get(request_url).json()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (list_of_comments, APP_ACCESS_TOKEN)
    print 'GET request url : &s' % (request_url)
    comment_list = requests.get(request_url).json()

    if comment_list['meta']['code'] == 200:
    if like_list['meta']['code'] == 200:
    if len((like_list['data'])>(comment_list['data'])):
        print 'this post is trending : %s'% (user_info['data'][0]['id'])
    else:
        print'status code other than 200 received'


# menu options of bot

def start_bot():
    while True:
     print '\n'
     print 'Instabot welcomes you'
     print 'choose from following :'
     print "a.Get my details\n"
     print "b.Get details of a user (by username)\n"
     print "c.Get your own recent post\n"
     print "d.Get the recent post of a user by username\n"
     print "e.Get a list of people who have liked the recent post of a user\n"
     print "f.Like the recent post of a user\n"
     print "g.Get a list of comments on the recent post of a user\n"
     print "h.Make a comment on the recent post of a user\n"
     print "j.Exit"

     choice = raw_input("Enter you choice: ")
     if choice == "a":
           own_info()
     elif choice == "b":
         insta_username = raw_input("Enter the username of the user: ")
         get_user_info(insta_username)
     elif choice == "c":
         get_own_post()
     elif choice == "d":
         insta_username = raw_input("Enter the username of the user: ")
         get_user_post(insta_username)
     elif choice == "e":
         insta_username = raw_input("Enter the username of the user: ")
         get_like_list(insta_username)
     elif choice == "f":
         insta_username = raw_input("Enter the username of the user: ")
         like_a_post(insta_username)
     elif choice == "g":
         insta_username = raw_input("Enter the username of the user: ")
         get_comment_list(insta_username)
     elif choice == "h":
         insta_username = raw_input("Enter the username of the user: ")
         post_a_comment(insta_username)
     elif choice == "j":
        exit()
    else:
     print "choice doesnt exist"

start_bot()




