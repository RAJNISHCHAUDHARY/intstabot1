import requests
from constant import BASE_URL,APP_ACCESS_TOKEN
from get_post_id import get_post_id
from get_user_post import get_user_post



def delete_a_comment(insta_username):
    comment_id = get_post_id(insta_username)
    #print comment_id
    media_id = get_post_id(insta_username)
    request_url = BASE_URL+"media/"+media_id+"/comments/"+comment_id+"?access_token="+APP_ACCESS_TOKEN
    delete_comment = requests.delete(request_url).json()
    if delete_a_comment['meta']['code'] == 200:
        print '\n...Comment IS deleted....'
    else:
        print 'Your Deletion of comment  was unsuccessful. Try again!'
