###########requirements################

#pygeocoder
sudo pip install geocoder

#pycurl
sudo aptitude install python-pycurl

# couchdb python client
wget http://pypi.python.org/packages/2.6/C/CouchDB/CouchDB-0.8-py2.6.egg
sudo easy_install CouchDB-0.8-py2.6.egg


####################running the application ######################
# python  tweets_geocoder.py --couchdb_ip=115.146.95.99:5984 --dbname_from='tweets' --dbname_to='yasmeen-test-tweets'
