from flask_sqlalchemy import SQLAlchemy
import datetime
# from sqlalchemy import Date

db = SQLAlchemy()

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    states = db.relationship('State', backref='Country', lazy=True) 

    def __repr__(self):
        return f'<Countries {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,       
        }


class State(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    cities = db.relationship('City', backref='State', lazy=True)
    def __repr__(self):
        return f'<States {self.name}>'
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "country_id": self.country_id,            
        }


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'), nullable=False)
    users = db.relationship('User', backref='City', lazy=True)
    establishments = db.relationship('Establishment', backref='City', lazy=True)
    bands = db.relationship('Band', backref='City', lazy=True)

    def __repr__(self):
        return f'<Cities {self.name}>'
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "state_id": self.state_id,
            # "locales": [locales.serialize() for local in self.locales]
        }
        


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    profile_img = db.Column(db.String(255), nullable=True)
    portrait_img = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=True)
    artistic_name = db.Column(db.String(80), nullable=True)
    description = db.Column(db.String(500), nullable=True)
    youtube_url = db.Column(db.String(80), nullable=True)
    spotify_url = db.Column(db.String(80), nullable=True)
    website_url = db.Column(db.String(80), nullable=True)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=True)
    establishments = db.relationship("Establishment", backref="User", lazy=True)
    user_bands = db.relationship('UserBand', backref='User', lazy=True) 
    user_instrument = db.relationship("UserInstrument", backref="User", lazy=True)
    music_genre_user = db.relationship("MusicGenreUser", backref="User", lazy=True)
    posts = db.relationship("Post", backref="User", lazy=True)
    comments = db.relationship("Comment", backref="User", lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "profile_img": self.profile_img,
            "portrait_img": self.portrait_img,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "artistic_name": self.artistic_name,
            "description": self.description,
            "youtube_url": self.youtube_url,
            "spotify_url": self.spotify_url,
            "website_url": self.website_url,
            "city_id": self.city_id,
          
        }

class InstrumentCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    instruments = db.relationship("Instrument", backref="InstrumentCategory", lazy=True)

    def __repr__(self):
        return f'<InstrumentCategory {self.name}>'

    def serialize(self):
        return {
            "name": self.name,
        }

class Instrument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    instrument_category_id = db.Column(db.Integer, db.ForeignKey('instrument_category.id'), nullable=False)
    user_instrument = db.relationship("UserInstrument", backref="Instrument", lazy=True)
    band_instrument = db.relationship("BandInstrument", backref="Instrument", lazy=True)

    def __repr__(self):
        return f'<Instrument {self.name}>'

    def serialize(self):
        return {
            "name": self.name,
            "instrument_category_id": self.instrument_category_id,
        }



class MusicGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    music_genre_establishment = db.relationship("MusicGenreEstablishment", backref="MusicGenre", lazy=True)
    music_genre_event = db.relationship("MusicGenreEvent", backref="MusicGenre", lazy=True)
    music_genre_user = db.relationship("MusicGenreUser", backref="MusicGenre", lazy=True)
    music_genre_band = db.relationship("MusicGenreBand", backref="MusicGenre", lazy=True) 

    def __repr__(self):
        return f'<MusicGenre {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,            
        }

class Band(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    band_profile_img = db.Column(db.String(255), nullable=True)
    band_portrait_img = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    user_bands = db.relationship('UserBand', backref='Band', lazy=True)
    band_instrument = db.relationship("BandInstrument", backref="Band", lazy=True) 
    music_genre_band = db.relationship("MusicGenreBand", backref="Band", lazy=True) 
    
    def __repr__(self):
        return f'<Band {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "band_profile_img": self.band_profile_img,
            "band_portrait_img": self.band_portrait_img,
            "name": self.name,
            "description": self.description,
        }



class Establishment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    establishment_profile_img = db.Column(db.String(255), nullable=True)
    establishment_portrait_img = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(80), nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(80), nullable=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    events = db.relationship("Event", backref="Establishment", lazy=True) 
    music_genre_establishment = db.relationship("MusicGenreEstablishment", backref="Establishment", lazy=True)
    
    def __repr__(self):
        return f'<Establishment {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "establishment_profile_img": self.establishment_profile_img,
            "establishment_portrait_img": self.establishment_portrait_img,
            "name": self.name,
            "description": self.description,
            "user_id": self.user_id,
        }

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_profile_img = db.Column(db.String(255), nullable=True)
    event_portrait_img = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=True)
    establishment_id = db.Column(db.Integer, db.ForeignKey('establishment.id'), nullable=False)
    music_genre_event = db.relationship("MusicGenreEvent", backref="Event", lazy=True)
    
    def __repr__(self):
        return f'<Event {self.name}>'

    def serialize(self):
        music_genre_event_list = []
        for music_genre in self.music_genre_event:
            music_genre_event_list.append(music_genre.serialize())
        return {
            "id": self.id,
            "event_profile_img": self.event_profile_img,
            "event_portrait_img": self.event_portrait_img,
            "name": self.name,
            "description": self.description,
            "establishment_id": self.establishment_id,
            "music_genre_event": music_genre_event_list,
            "establishment_name": Establishment.query.get(self.establishment_id).name
        }

class UserBand(db.Model): #intermedia
    id = db.Column(db.Integer, primary_key=True)
    band_id = db.Column(db.Integer, db.ForeignKey('band.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<UserBand {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "band_id": self.band_id,
            "user_id": self.user_id,
        }


class UserInstrument(db.Model): #intermedia
    id = db.Column(db.Integer, primary_key=True)
    instrument_id = db.Column(db.Integer, db.ForeignKey('instrument.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<UserInstrument {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "instrument_id": self.instrument_id,
            "user_id": self.user_id,
        }


class BandInstrument(db.Model): #intermedia
    id = db.Column(db.Integer, primary_key=True)
    instrument_id = db.Column(db.Integer, db.ForeignKey('instrument.id'), nullable=False)
    band_id = db.Column(db.Integer, db.ForeignKey('band.id'), nullable=False)

    def __repr__(self):
        return f'<BandInstrument {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "instrument_id": self.instrument_id,
            "band_id": self.band_id,
        }

class MusicGenreEstablishment(db.Model): #intermedia
    id = db.Column(db.Integer, primary_key=True)
    music_genre_id = db.Column(db.Integer, db.ForeignKey('music_genre.id'), nullable=False)
    establishment_id = db.Column(db.Integer, db.ForeignKey('establishment.id'), nullable=False)

    def __repr__(self):
        return f'<MusicGenreEstablishment {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "music_genre_id": self.music_genre_id,
            "establishment_id": self.establishment_id,
        }

class MusicGenreEvent(db.Model): #intermedia
    id = db.Column(db.Integer, primary_key=True)
    music_genre_id = db.Column(db.Integer, db.ForeignKey('music_genre.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

    def __repr__(self):
        return f'<MusicGenreEvent {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "music_genre_id": self.music_genre_id,
            "event_id": self.event_id,
        }


class MusicGenreUser(db.Model): #intermedia
    id = db.Column(db.Integer, primary_key=True)
    music_genre_id = db.Column(db.Integer, db.ForeignKey('music_genre.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<MusicGenreUser {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "music_genre_id": self.music_genre_id,
            "user_id": self.user_id,
        }


class MusicGenreBand(db.Model): #intermedia
    id = db.Column(db.Integer, primary_key=True)
    music_genre_id = db.Column(db.Integer, db.ForeignKey('music_genre.id'), nullable=False)
    band_id = db.Column(db.Integer, db.ForeignKey('band.id'), nullable=False)

    def __repr__(self):
        return f'<MusicGenreBand {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "music_genre_id": self.music_genre_id,
            "band_id": self.band_id,
        }


class Post(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(80), nullable=True)
    created_at = db.Column(db.DateTime, nullable = False , default = datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable = False , default = datetime.datetime.utcnow)
    post_img = db.Column(db.String(255), nullable=True)
    post_video = db.Column(db.String(255), nullable=True)
    

    def __repr__(self):
        return f'<Post {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "post_img": self.post_img,
            "post_video": self.post_video,
        }

class Comment(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    description = db.Column(db.String(80), nullable=True)
    created_at = db.Column(db.DateTime, nullable = False , default = datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable = False , default = datetime.datetime.utcnow)

    def __repr__(self):
        return f'<Comment {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "post_id": self.post_id,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }