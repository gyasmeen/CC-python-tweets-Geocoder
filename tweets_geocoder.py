#run the applicaiton
# python  tweets_geocoder.py --couchdb_ip=115.146.95.99:5984 --dbname_from='tweets' --dbname_to='yasmeen-test-tweets'
from couchdb import Server
from csv import DictWriter
from csv import DictReader
#import geocoder
#from geopy import geocoders
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from time import sleep

def geo_AurinDataset(csv_file):
    pos_tweets=[]
    neg_tweets=[]
    senti=[]
    tweets_samples=[]
    #csv_file='Sentiment Analysis Dataset.csv'
    with open(csv_file) as f:
        for row in DictReader(f):
            feat_name= row["feature_name"]
	    g = geocoder.google(feat_name+', vic')
	    print g.latlng
	    print g.geojson['bbox']

def not_exist(tw_id):

    tweets_list = db1.view('sentiment-analysis/get_tweet_ids')
    for row in tweets_list:
	#	print  type (row['key']), row['key'], tw_id
	if (row['key']== tw_id):
	    return "false"
    return "true"

import argparse


parser = argparse.ArgumentParser(description='')
parser.add_argument('--couchdb_ip', '-ip', help='ip of couchdb')
parser.add_argument('--dbname_from', '-from_db', help='from db name')
parser.add_argument('--dbname_to', '-to_db', help='to db name')

args = parser.parse_args()


server = Server("http://"+args.couchdb_ip+"/")
db = server[args.dbname_from]
db1 = server[args.dbname_to]

def geo_tweets():

    geolocator = Nominatim()
    count =1
    tweets_list = db1.view('sentiment-analysis/get_tweet_ids')
    for doc in  db.view('sentiment-analysis/get_alltweets'):
        tw=doc.value
        if  (not_exist(tw['id'])== "true"):
    	    loc_point= tw['geo']
	    #print loc_point
	    try:
                location = geolocator.geocode(loc_point['coordinates'])
	        #print type(location)
	        try:
   	            print count ,location.address
                    modified_place={'geo_address': location.address}
                    place_update = {'place-mod': modified_place}
	            new_tw = tw.copy()
                    new_tw.update(place_update)
                    new_tw.update({'_id': tw['id_str']})
                    try:
                        db1.save(new_tw)
                    except:
                        print ("Tweet " + tw['id_str'] + " already exists !!!! " )
	        except:
                    print ("Returned Location is Empty !!!! " )
            except GeocoderTimedOut as e:
	        print("Error: geocode faied on input %s with message ")
		print loc_point['coordinates']
	else:
    	    print count, 'ALREADY EXIST!!'
        count =count+1

geo_tweets()
