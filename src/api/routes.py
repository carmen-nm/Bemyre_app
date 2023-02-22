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



# RELLENADO DE TABLAS SIN JWT NI TOKEN
@api.route('/country', methods=['POST'])
def add_country():
    data = request.json()
    new_country = Country(
        name = data["name"],        
    )
    db.session.add(new_country)
    db.session.commit()
    response_body = {
        "msg": "country añadido"
    }
    return jsonify(response_body), 200


@api.route('/state', methods=['POST'])
def add_country():
    data = request.json()
    new_state = State(
        name = data["name"],
        country_id = data["country_id"]    
    )
    db.session.add(new_state)
    db.session.commit()
    response_body = {
        "msg": "state añadido"
    }
    return jsonify(response_body), 200


@api.route('/city', methods=['POST'])
def add_city():
    data = request.json()
    new_city = City(
        name = data["name"],
        state_id = data["state_id"]    
    )
    db.session.add(new_city)
    db.session.commit()
    response_body = {
        "msg": "city añadida"
    }
    return jsonify(response_body), 200


@api.route('/user', methods=['POST'])
def add_user():
    data = request.json()
    new_user = User(
        user_name = data["user_name"],
        profile_img = data["profile_img"],
        portrait_img = data["portrait_img"],
        email = data["email"], 
        password = data["password"],
        first_name = data["first_name"],
        last_name = data["last_name"],
        artistic_name = data["artistic_name"],
        youtube_url = data["youtube_url"],
        spotify_url = data["spotify_url"],
        website_url = data["website_url"],
        is_active = data["is_active"],
        city_id = data["city_id"],
    )
    db.session.add(new_user)
    db.session.commit()
    response_body = {
        "msg": "user añadido"
    }
    return jsonify(response_body), 200


@api.route('/instrumentcategory', methods=['POST'])
def add_instrumentcategory():
    data = request.json()
    new_instrumentcategory = InstrumentCategory(
        name = data["name"],
    )
    db.session.add(new_instrumentcategory)
    db.session.commit()
    response_body = {
        "msg": "instrumentcategory añadida"
    }
    return jsonify(response_body), 200


@api.route('/instrument', methods=['POST'])
def add_instrument():
    data = request.json()
    new_instrument = Instrument(
        name = data["name"],
        instrument_category_id = data["instrument_category_id"]
    )
    db.session.add(new_instrument)
    db.session.commit()
    response_body = {
        "msg": "instrument añadido"
    }
    return jsonify(response_body), 200


@api.route('/musicgenre', methods=['POST'])
def add_musicgenre():
    data = request.json()
    new_musicgenre = MusicGenre(
        name = data["name"],        
    )
    db.session.add(new_musicgenre)
    db.session.commit()
    response_body = {
        "msg": "musicgenre añadido"
    }
    return jsonify(response_body), 200


@api.route('/band', methods=['POST'])
def add_band():
    data = request.json()
    new_band = Band(
        band_profile_img = data["band_profile_img"],
        band_portrait_img = data["band_portrait_img"],
        name = data["name"],
        description = data["description"],
        city_id = data["city_id"],               
    )
    db.session.add(new_band)
    db.session.commit()
    response_body = {
        "msg": "band añadida"
    }
    return jsonify(response_body), 200


@api.route('/establishment', methods=['POST'])
def add_establishment():
    data = request.json()
    new_establishment = Establishment(
        establishment_profile_img = data["establishment_profile_img"],
        establishment_portrait_img = data["establishment_portrait_img"],
        name = data["name"],
        description = data["description"],
        ubicacion = data["ubicacion"],
        city_id = data["city_id"],
        user_id = data["user_id"],          
    )
    db.session.add(new_establishment)
    db.session.commit()
    response_body = {
        "msg": "establishment añadido"
    }
    return jsonify(response_body), 200


@api.route('/event', methods=['POST'])
def add_event():
    data = request.json()
    new_event = Event(
        event_profile_img = data["event_profile_img"],
        event_portrait_img = data["event_portrait_img"],
        name = data["name"],
        description = data["description"],    
        establishment_id = data["establishment_id"],   
        date = data["date"],   
    )
    db.session.add(new_event)
    db.session.commit()
    response_body = {
        "msg": "event añadido"
    }
    return jsonify(response_body), 200


@api.route('/userband', methods=['POST'])
def add_userband():
    data = request.json()
    new_userband = UserBand(
        band_id = data["band_id"],
        user_id = data["user_id"],
    )
    db.session.add(new_userband)
    db.session.commit()
    response_body = {
        "msg": "userband añadido"
    }
    return jsonify(response_body), 200

@api.route('/userinstrument', methods=['POST'])
def add_userinstrument():
    data = request.json()
    new_userinstrument = UserInstrument(
        instrument_id = data["instrument_id"],
        user_id = data["user_id"],
    )
    db.session.add(new_userinstrument)
    db.session.commit()
    response_body = {
        "msg": "userinstrument añadido"
    }
    return jsonify(response_body), 200

@api.route('/bandinstrument', methods=['POST'])
def add_bandinstrument():
    data = request.json()
    new_bandinstrument = BandInstrument(
        instrument_id = data["instrument_id"],
        band_id = data["band_id"],
    )
    db.session.add(new_bandinstrument)
    db.session.commit()
    response_body = {
        "msg": "bandinstrument añadido"
    }
    return jsonify(response_body), 200

@api.route('/musicgenreestablishment', methods=['POST'])
def add_musicgenreestablishment():
    data = request.json()
    new_musicgenreestablishment = MusicGenreEstablishment(
        music_genre_id = data["music_genre_id"],
        establishment_id = data["establishment_id"],
    )
    db.session.add(new_musicgenreestablishment)
    db.session.commit()
    response_body = {
        "msg": "musicgenreestablishment añadido"
    }
    return jsonify(response_body), 200


@api.route('/musicgenreevent', methods=['POST'])
def add_musicgenreevent():
    data = request.json()
    new_musicgenreevent = MusicGenreEvent(
        music_genre_id = data["music_genre_id"],
        event_id = data["event_id"],
    )
    db.session.add(new_musicgenreevent)
    db.session.commit()
    response_body = {
        "msg": "musicgenreevent añadido"
    }
    return jsonify(response_body), 200

@api.route('/musicgenreuser', methods=['POST'])
def add_musicgenreuser():
    data = request.json()
    new_musicgenreuser = MusicGenreUser(
        music_genre_id = data["music_genre_id"],
        user_id = data["user_id"],
    )
    db.session.add(new_musicgenreuser)
    db.session.commit()
    response_body = {
        "msg": "musicgenreuser añadido"
    }
    return jsonify(response_body), 200


@api.route('/musicgenreband', methods=['POST'])
def add_musicgenreband():
    data = request.json()
    new_musicgenreband = MusicGenreBand(
        music_genre_id = data["music_genre_id"],
        band_id = data["band_id"],
    )
    db.session.add(new_musicgenreband)
    db.session.commit()
    response_body = {
        "msg": "musicgenreband añadido"
    }
    return jsonify(response_body), 200


@api.route('/post', methods=['POST'])
def add_post():
    data = request.json()
    new_post = Post(
        user_id = data["user_id"],
        description = data["description"],
        created_at = data["created_at"],
        updated_at = data["updated_at"],
        post_img = data["post_img"],
        post_video = data["post_video"],
    )
    db.session.add(new_post)
    db.session.commit()
    response_body = {
        "msg": "post añadido"
    }
    return jsonify(response_body), 200


@api.route('/comment', methods=['comment'])
def add_comment():
    data = request.json()
    new_comment = Comment(
        user_id = data["user_id"],
        description = data["description"],
        created_at = data["created_at"],
        updated_at = data["updated_at"],
        post_id = data["post_id"],        
    )
    db.session.add(new_comment)
    db.session.commit()
    response_body = {
        "msg": "comment añadido"
    }
    return jsonify(response_body), 200


# pintar cards eventos
@api.route('/events', methods=['GET'])
def get_events():     
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
