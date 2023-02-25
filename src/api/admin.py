  
import os
from flask_admin import Admin
from .models import db, User, Country, State, City, InstrumentCategory, Instrument, MusicGenre, Band, Establishment, Event, UserInstrument, UserBand, MusicGenreEstablishment, MusicGenreEvent, MusicGenreUser, MusicGenreBand
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Country, db.session))
    admin.add_view(ModelView(State, db.session))
    admin.add_view(ModelView(City, db.session))
    admin.add_view(ModelView(InstrumentCategory, db.session))
    admin.add_view(ModelView(Instrument, db.session))
    admin.add_view(ModelView(MusicGenre, db.session))
    admin.add_view(ModelView(Band, db.session))
    admin.add_view(ModelView(Establishment, db.session))
    admin.add_view(ModelView(Event, db.session))
    admin.add_view(ModelView(UserInstrument, db.session))
    admin.add_view(ModelView(UserBand, db.session))
    admin.add_view(ModelView(MusicGenreEstablishment, db.session))
    admin.add_view(ModelView(MusicGenreEvent, db.session))
    admin.add_view(ModelView(MusicGenreUser, db.session))
    admin.add_view(ModelView(MusicGenreBand, db.session))
    # admin.add_view(ModelView(Post, db.session))
    # admin.add_view(ModelView(Comment, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))