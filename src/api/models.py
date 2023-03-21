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
        }
        


# integrantes_table = db.Table('integrantes_table',
#   db.Column('owner_id', db.Integer, db.ForeignKey('member.id')),
#   db.Column('member_id', db.Integer, db.ForeignKey('owner.id'))
# )



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    profile_img = db.Column(db.String(700), nullable=True)
    portrait_img = db.Column(db.String(700), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=True)
    artistic_name = db.Column(db.String(80), nullable=True)
    description = db.Column(db.String(700), nullable=True)
    youtube_url = db.Column(db.String(700), nullable=True)
    spotify_url = db.Column(db.String(700), nullable=True)
    website_url = db.Column(db.String(700), nullable=True)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=True)
    establishments = db.relationship("Establishment", backref="User", lazy=True)
    bands = db.relationship("Band", backref="User", lazy=True)
    user_bands = db.relationship('UserBand', backref='User', lazy=True) 
    user_instrument = db.relationship("UserInstrument", backref="User", lazy=True)
    music_genre_user = db.relationship("MusicGenreUser", backref="User", lazy=True)
    # posts = db.relationship("Post", backref="User", lazy=True)
    # comments = db.relationship("Comment", backref="User", lazy=True)
    user_forms_in_demand = db.relationship("UserFormsInDemand", backref="User", lazy=True) 
    # integrantes  = db.relationship('Band',
    #     secondary = integrantes_table,
    #     primaryjoin = ('integrantes_table.c.owner_id == id'), 
    #     secondaryjoin = ('integrantes_table.c.member_id == id'),
    #     backref = db.backref('User', lazy = 'dynamic'),
    #     lazy = 'dynamic')


    # def integrantes_member(self, listing):
    #     if not self.is_favorite(listing):
    #     self.favorites.append(listing)
    #     return self

    # def unfavorite_listing(self, listing):
    #     if self.is_favorite(listing):
    #     self.favorites.remove(listing)
    #     return self

    # def is_favorite(self, listing):
    #     return self.favorites.filter(favorites_table.c.listing_id == listing.id).count() > 0

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        # instrument = Intrument.query.filter_by
        # instrument_list= []
        # for user_ins in user_instrument:
        #     instrument_list.append(user_ins.serialize())

        city = City.query.filter_by(id=self.city_id).first()
        # user_instrument = UserInstrument.query.filter_by(user_id=self.id).first()
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
            "city": city.name,
            "music_genre_user": [music_genre.serialize() for music_genre in self.music_genre_user],
            # "user_instrument": user_instrument.instrument_name
            # "instrument": instrument_list
            # "instrument": user_instrument.instrument_name
            "user_instrument": [user_instru.serialize() for user_instru in self.user_instrument],
            # "user_instrument": user_instrument.serialize()
            # "bands": [band.serialize() for band in self.bands],
            "establishments": [establishment.serialize() for establishment in self.establishments]

          
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
    # band_instrument = db.relationship("BandInstrument", backref="Instrument", lazy=True)
    in_demand = db.relationship('InDemand', backref='Instrument', lazy=True)


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
    description = db.Column(db.String(700), nullable=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    user_bands = db.relationship('UserBand', backref='Band', lazy=True)
    music_genre_band = db.relationship("MusicGenreBand", backref="Band", lazy=True) 
    # podria poner user_id de nuevo pero que fuese una foreinkey normal para el owner?
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    in_demand = db.relationship('InDemand', backref='Band', lazy=True)


    def __repr__(self):
        return f'<Band {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "band_profile_img": self.band_profile_img,
            "band_portrait_img": self.band_portrait_img,
            "name": self.name,
            "description": self.description,
            "music_genre_band": [music_genre.serialize() for music_genre in self.music_genre_band],
            "owner_id": self.owner_id,
            "city": City.query.get(self.city_id).name
        }

class InDemand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    forms_in_demand = db.relationship("FormsInDemand", backref="InDemand", lazy=True) 
    band_id = db.Column(db.Integer, db.ForeignKey('band.id'), nullable=False)
    instrument_id = db.Column(db.Integer, db.ForeignKey('instrument.id'), nullable=False)
    description = db.Column(db.String(700), nullable=True)

    def __repr__(self):
        return f'<InDemand {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "band_profile_img": self.band_profile_img,
            # pillar la city de la band
            # pillar lso generos de musica de la band
            # el intrument se registra con el id aunq se seleccione con un get desde el nombre
        }



class FormsInDemand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    in_demand_id = db.Column(db.Integer, db.ForeignKey('in_demand.id'), nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    availability = db.Column(db.String(700), nullable=True)
    residence = db.Column(db.String(700), nullable=True)
    experience  = db.Column(db.String(700), nullable=True)
    moreinfo = db.Column(db.String(700), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    user_forms_in_demand = db.relationship("UserFormsInDemand", backref="FormsInDemand", lazy=True) 


    def __repr__(self):
        return f'<FormsInDemand {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "availability": self.availability,
            "residence": self.residence,
            "experience": self.experience,
            "moreinfo": self.moreinfo,
            "age": self.age,
            # pillar el instrumento del user (inamovibles)
            # pillar lso generos de musica del user (inamovibles)
        }


class UserFormsInDemand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    forms_in_demand_id = db.Column(db.Integer, db.ForeignKey('forms_in_demand.id'), nullable=False)

    def __repr__(self):
        return f'<UserFormsInDemand {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "forms_in_demand_id": self.forms_in_demand_id,
        }



class Establishment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    establishment_profile_img = db.Column(db.String(255), nullable=True)
    establishment_portrait_img = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(80), nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(700), nullable=True)
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
            "ubicacion": self.ubicacion,
            "user_id": self.user_id,
            "city": City.query.get(self.city_id).name,
            "music_genre_establishment": [music_genre.serialize() for music_genre in self.music_genre_establishment],
        }

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_profile_img = db.Column(db.String(550), nullable=True)
    event_portrait_img = db.Column(db.String(550), nullable=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(700), nullable=True)
    establishment_id = db.Column(db.Integer, db.ForeignKey('establishment.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=True)
    music_genre_event = db.relationship("MusicGenreEvent", backref="Event", lazy=True)
    
    def __repr__(self):
        return f'<Event {self.name}>'
 
    def serialize(self):

        music_genre_event_list = []
        for music_genre in self.music_genre_event:
            music_genre_event_list.append(music_genre.serialize())

        city_id = Establishment.query.get(self.establishment_id).city_id
        # print(city_id)
        city = City.query.filter_by(id=city_id).first()
        # print(city.serialize())
            
        return {
            "id": self.id,
            "event_profile_img": self.event_profile_img,
            "event_portrait_img": self.event_portrait_img,
            "name": self.name,
            "description": self.description,
            "establishment_id": self.establishment_id,
            "music_genre_event": music_genre_event_list,
            "date": self.date.strftime("%m/%d/%Y"),
            "establishment_name": Establishment.query.get(self.establishment_id).name,            
            "ubicacion": Establishment.query.get(self.establishment_id).ubicacion,
            "city": city.name,
            "hour": self.date.strftime("%H:%M")
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
            "instrument_name": Instrument.query.get(self.instrument_id).name
        }


# class BandInstrument(db.Model): #intermedia
#     id = db.Column(db.Integer, primary_key=True)
#     instrument_id = db.Column(db.Integer, db.ForeignKey('instrument.id'), nullable=False)
#     band_id = db.Column(db.Integer, db.ForeignKey('band.id'), nullable=False)

#     def __repr__(self):
#         return f'<BandInstrument {self.id}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "instrument_id": self.instrument_id,
#             "band_id": self.band_id,
#         }

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
            "music_genre_name": MusicGenre.query.get(self.music_genre_id).name
        }

class MusicGenreEvent(db.Model): #intermedia
    id = db.Column(db.Integer, primary_key=True)
    music_genre_id = db.Column(db.Integer, db.ForeignKey('music_genre.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    # music_genre = db.relationship("MusicGenre", backref="MusicGenreEvent", lazy=True)

    def __repr__(self):
        return f'<MusicGenreEvent {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "music_genre_id": self.music_genre_id,
            "event_id": self.event_id,
            # "music_genre_name": self.music_genre.name,
            "music_genre_name": MusicGenre.query.get(self.music_genre_id).name
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
            "music_genre_name": MusicGenre.query.get(self.music_genre_id).name
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
            "music_genre_name": MusicGenre.query.get(self.music_genre_id).name
        }


# class Post(db.Model): 
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     description = db.Column(db.String(80), nullable=True)
#     created_at = db.Column(db.DateTime, nullable = False , default = datetime.datetime.utcnow)
#     updated_at = db.Column(db.DateTime, nullable = False , default = datetime.datetime.utcnow)
#     post_img = db.Column(db.String(255), nullable=True)
#     post_video = db.Column(db.String(255), nullable=True)
    

#     def __repr__(self):
#         return f'<Post {self.id}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "user_id": self.user_id,
#             "description": self.description,
#             "created_at": self.created_at,
#             "updated_at": self.updated_at,
#             "post_img": self.post_img,
#             "post_video": self.post_video,
#         }

# class Comment(db.Model): 
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
#     description = db.Column(db.String(80), nullable=True)
#     created_at = db.Column(db.DateTime, nullable = False , default = datetime.datetime.utcnow)
#     updated_at = db.Column(db.DateTime, nullable = False , default = datetime.datetime.utcnow)

#     def __repr__(self):
#         return f'<Comment {self.id}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "user_id": self.user_id,
#             "post_id": self.post_id,
#             "description": self.description,
#             "created_at": self.created_at,
#             "updated_at": self.updated_at,
#         }