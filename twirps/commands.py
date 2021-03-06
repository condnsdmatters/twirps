from __future__ import unicode_literals
import json
import logging
import os

from archipelago import archipelago, setup

from flask import Blueprint, Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, Response

from twirps import app, data_collection

from twirps.classes import TDBHandler, NeoDBHandler, PgDBHandler
from decorators import requires_auth

LOGGER = logging.getLogger(__name__)

def initialise_databases():
    db_handler = TDBHandler()
    db_handler.initialise_neo_db()
    db_handler.initialise_pg_db()

def destroy_databases():
    db_handler = TDBHandler()
    db_handler.drop_pg_db()
    db_handler.drop_neo_db()

def start_streamer():
    data_collection.start_stream()
    pass

def stop_streamer():
    pass

def start_bulk_historical_collection(max_tweets=100, tweet_buffer=5, tweet_resolution=1000):
    data_collection.get_bulk_tweets_main(max_tweets, tweet_buffer, tweet_resolution)
    pass

def stop_bulk_historical_collection():
    pass

def load_passive_twirps_to_database_by_handle():
    pass

def load_active_twirps_to_database_by_handle():
    pass

def load_mp_twirps_to_database():
    data_collection.get_bulk_twirps_main()

def start_bulk_recent_collection():
    pass

def storp_bulk_recent_collection():
    pass

def delete_data():
    pass

def initialise_postgres_db():
    db_handler = PgDBHandler()
    db_handler.create_tables()

def drop_postgres_db():
    db_handler = PgDBHandler()
    db_handler.drop_tables()

def initialise_neo_db():
    db_handler = NeoDBHandler()
    db_handler.init_constraints()

def drop_neo_db():
    db_handler = NeoDBHandler()
    db_handler.delete_graph_data()
    db_handler.remove_constraints()
    pass

def refresh_archipelago():
    setup.setup_archipelago(os.environ['ARCHIPELAGO_DB'])

def sync_subscribers_from_twitter():
    pass

def sync_subcribers_to_twitter():
    pass

def subscribe_all_twirps_to_twitter():
    data_collection.subscribe_friends_from_twirps()

def sync_neo_with_arch():
    data_collection.sync_neo_with_arch()

def resync_tweets_pg_to_neo():
    db_handler = TDBHandler()
    db_handler.resync_tweets_pg_to_neo()




