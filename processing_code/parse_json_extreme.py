import json
import time
import sys

fileN = sys.argv[1]

fO = open(fileN[:-5]+".tsv", "w")
with open(fileN, 'r') as f:
    cnt=1
    for cnt, line in enumerate(f):
        try:
            tweet = json.loads(line) # load it as Python dict
        except: 
            continue
        try:
            tweet_created_at=str(tweet["created_at"])
        except:
            tweet_created_at='NULL'
        try:
            tweet_id=str(tweet["id"])
        except:
            tweet_id='NULL'
        try:
            tweet_id_str=str(tweet["id_str"])
        except:
            tweet_id_str='NULL'
        try:
            tweet_text=str(tweet["text"])
        except:
            tweet_text='NULL'
        try:
            tweet_truncated=str(tweet["truncated"])
        except:
            tweet_truncated='NULL'
        try:
            tweet_source=str(tweet["source"])
        except:
            tweet_source='NULL'
        try:
            tweet_in_reply_to_status_id=str(tweet["in_reply_to_status_id"])
        except:
            tweet_in_reply_to_status_id='NULL'
        try:
            tweet_in_reply_to_status_id_str=str(tweet["in_reply_to_status_id_str"])
        except:
            tweet_in_reply_to_status_id_str='NULL'
        try:
            tweet_in_reply_to_user_id=str(tweet["in_reply_to_user_id"])
        except:
            tweet_in_reply_to_user_id='NULL'
        try:
            tweet_in_reply_to_user_id_str=str(tweet["in_reply_to_user_id_str"])
        except:
            tweet_in_reply_to_user_id_str='NULL'
        try:
            tweet_in_reply_to_screen_name=str(tweet["in_reply_to_screen_name"])
        except:
            tweet_in_reply_to_screen_name='NULL'
        try:
            tweet_geo=str(tweet["geo"])
        except:
            tweet_geo='NULL'
        try:
            tweet_coordinates=str(tweet["coordinates"])
        except:
            tweet_coordinates='NULL'
        try:
            tweet_place=str(tweet["place"])
        except:
            tweet_place='NULL'
        try:
            tweet_contributors=str(tweet["contributors"])
        except:
            tweet_contributors='NULL'
        try:
            tweet_user_id=str(tweet["user"]["id"])
        except:
            tweet_user_id='NULL'
        try:
            tweet_user_id_str=str(tweet["user"]["id_str"])
        except:
            tweet_user_id_str='NULL'
        try:
            tweet_user_name=str(tweet["user"]["name"])
        except:
            tweet_user_name='NULL'
        try:
            tweet_user_screen_name=str(tweet["user"]["screen_name"])
        except:
            tweet_user_screen_name='NULL'
        try:
            tweet_user_location=str(tweet["user"]["location"])
        except:
            tweet_user_location='NULL'
        try:
            tweet_user_description=str(tweet["user"]["description"])
        except:
            tweet_user_description='NULL'
        try:
            tweet_place_id=str(tweet["place"]["id"])
        except:
            tweet_place_id='NULL'
        try:
            tweet_place_url=str(tweet["place"]["url"])
        except:
            tweet_place_url='NULL'
        try:
            tweet_place_place_type=str(tweet["place"]["place_type"])
        except:
            tweet_place_place_type='NULL'
        try:
            tweet_place_name=str(tweet["place"]["name"])
        except:
            tweet_place_name='NULL'
        try:
            tweet_place_full_name=str(tweet["place"]["full_name"])
        except:
            tweet_place_full_name='NULL'
        try:
            tweet_place_country_code=str(tweet["place"]["country_code"])
        except:
            tweet_place_country_code='NULL'
        try:
            tweet_place_country=str(tweet["place"]["country"])
        except:
            tweet_place_country='NULL'
        try:
            tweet_place_contained_within=str(tweet["place"]["contained_within"])
        except:
            tweet_place_contained_within='NULL'
        try:
            tweet_place_bounding_box_type=str(tweet["place"]["bounding_box"]["type"])
        except:
            tweet_place_bounding_box_type='NULL'
        try:
            tweet_place_bounding_box_coordinates=str(tweet["place"]["bounding_box"]["coordinates"])
        except:
            tweet_place_bounding_box_coordinates='NULL'
        try:
            tweet_geo_type=str(tweet["geo"]["type"])
        except:
            tweet_geo_type='NULL'
        try:
            tweet_geo_coordinates=str(tweet["geo"]["coordinates"])
        except:
            tweet_geo_coordinates='NULL'
        try:
            tweet_coordinates_type=str(tweet["coordinates"]["types"])
        except:
            tweet_coordinates_type='NULL'
        try:
            tweet_coordinates_coordinates=str(tweet["coordinates"]["coordinates"])
        except:
            tweet_coordinates_coordinates='NULL'
            
    ### added retweet_count and favorite_count
        try:
            retweet_count=str(tweet["retweet_count"])
        except:
            retweet_count='NULL'

        try:
            favorite_count=str(tweet["favorite_count"])
        except:
            favorite_count='NULL'

###


        objectString = tweet_created_at + "\t" + tweet_id + "\t" + tweet_id_str + "\t" + tweet_text + "\t" + tweet_truncated + "\t" + tweet_source + "\t" + tweet_in_reply_to_status_id + "\t" + tweet_in_reply_to_status_id_str + "\t" + tweet_in_reply_to_user_id + "\t" + tweet_in_reply_to_user_id_str + "\t" + tweet_in_reply_to_screen_name + "\t" + tweet_geo + "\t" + tweet_coordinates + "\t" + tweet_place + "\t" + tweet_contributors + "\t" + tweet_user_id + "\t" + tweet_user_id_str + "\t" + tweet_user_name + "\t" + tweet_user_screen_name + "\t" + tweet_user_location + "\t" + tweet_user_description + "\t" + tweet_place_id + "\t" + tweet_place_url + "\t" + tweet_place_place_type + "\t" + tweet_place_name + "\t" + tweet_place_full_name + "\t" + tweet_place_country_code + "\t" + tweet_place_country + "\t" + tweet_place_contained_within + "\t" + tweet_place_bounding_box_type + "\t" + tweet_place_bounding_box_coordinates + "\t" + tweet_geo_type + "\t" + tweet_geo_coordinates + "\t" + tweet_coordinates_type + "\t" + tweet_coordinates_coordinates + "\t" + retweet_count + "\t" + favorite_count 
        objectString = objectString.replace('\n','')
        objectString = objectString.replace('\r','')		
        fO.write(objectString + "\n")
        cnt +=1
