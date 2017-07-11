#import matlotlib library
import matplotlib.pyplot as plt
#import file from wordcloud
from wordcloud import WordCloud
#import app access and base url from constant file
from constant import APP_ACCESS_TOKEN,BASE_URL
#import requests library
import requests


#create a function of analyse_media
def analyse_media(media_id, target_string, trends):
    #here is code logic
    request_url = BASE_URL + "media/%s?access_token=%s" % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    response = requests.get(request_url).json()

    if (response['meta']['code'] == 200):
        if len(response['data']['tags']) > 0:
            for cur_index in range(0, len(response['data']['tags'])):
                if response['data']['tags'][cur_index] in trends:
                    trends[response['data']['tags'][cur_index]] += 1
                else:
                    trends[response['data']['tags'][cur_index]] = 1
    else:
        print 'Error: not 200'


def find_sub_trends(target_string):
    request_url = BASE_URL + "tags/%s/media/recent?access_token=%s" % (target_string, APP_ACCESS_TOKEN)
    print "Looking for tags: %s" % (request_url)
    response = requests.get(request_url).json()

    if (response['meta']['code'] == 200):
        if len(response['data']) > 0:
            trends = {}

            fh = open("temp.txt", "w")

            for cur_index in range(0, len(response['data'])):
                cur_id = response["data"][cur_index]["id"]
                analyse_media(cur_id, target_string, trends)

            trends.pop(target_string.lower(), None)

            wordcloud = WordCloud().generate_from_frequencies(trends)

            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            plt.show()

        else:
            print "No posts found"
    else:
        print 'Error'