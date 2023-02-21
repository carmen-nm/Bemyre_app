"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Country, State, City, InstrumentCategory, Instrument, MusicGenre, Band, Establishment, Event, UserInstrument, BandInstrument, UserBand, MusicGenreEstablishment, MusicGenreEvent, MusicGenreUser, MusicGenreBand, Post, Comment
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/events', methods=['GET'])
def events():
    
    events = Event.query.all()

    print('hola', events)
    events_list = []
    print(events_list)
    for event in events:
        print('1', event)
        events_list.append(event.serialize())

        
    return jsonify(events_list), 200



# @api.route('/<int:genre_id>/event/', methods=['GET'])
# def musicGenre_event(genre_id):
   
#     events = MusicGenreEvent.query.filter_by(music_genre_id=genre_id).all()
#     print(events)
#     events = [event.serialize() for event in events]
#     return jsonify(events), 200
