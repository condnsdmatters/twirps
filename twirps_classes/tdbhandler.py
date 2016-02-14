import sqlite3
import os

class TDBHandler(object):
    def __init__(self, db_name='twirpy.db'):
        self.db_name = db_name

    def is_db_setup(self ):
        return os.path.isfile(self.db_name)

    def complete_reboot(self):
        if self.is_db_setup():
            os.remove(self.db_name)
        self.create_twirpy_db()

    def create_twirpy_db(self):
        '''Creates a database with tables for TweetData and TwirpData'''

        with sqlite3.connect(self.db_name) as connection:
            cur = connection.cursor()
            cur.execute('CREATE TABLE TweetData (UserID Number, UserHandle Text, FavouriteCount Number, \
                                                RetweetCount Number, Content Text, Retweet Text, \
                                                CreatedDate Text, TwitterID Number UNIQUE)')
            cur.execute('CREATE TABLE TwirpData (UserID Number UNIQUE, UserName Text, Name Text, Handle Text, \
                                                FollowersCount Number, FriendsCount Number,\
                                                TweetCount Number, RetweetCount Number, \
                                                BeenRetweeted Number, FavouriteHashtag Text, \
                                                HashtagCount Number, OfficialId Number)')
            cur.execute('CREATE TABLE TweetEntities (TweetID Number, UserID Number,\
                                                EntityType Text, Entity Text, ToUser Number,\
                                                UrlBase Text, UNIQUE(TweetID, UserID, EntityType, Entity) )')

            cur.execute('CREATE INDEX UserIDIndex ON TweetData (UserID)')
            cur.execute('CREATE INDEX UserIDEntityIndex ON TweetEntities (UserID)')

    def add_Twirp_to_database(self, Twirp):

        input_tuple =  (Twirp.id, Twirp.username, Twirp.name, Twirp.handle, Twirp.followers_count, 
                        Twirp.friends_count, Twirp.statuses, Twirp.retweet_count, 
                        Twirp.been_retweet_count, Twirp.favourite_hashtag,
                        Twirp.hashtag_count, Twirp.official_id)
        print Twirp.name
        with sqlite3.connect(self.db_name) as connection:
            cur = connection.cursor()
            cur.execute('INSERT OR REPLACE INTO TwirpData\
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?) ', input_tuple)

    def get_stored_mps_names(self):
        with sqlite3.connect(self.db_name) as connection:
            cur = connection.cursor()
            cur.execute('SELECT  Name  FROM TwirpData')

        return [ name[0] for name in cur.fetchall() ]

