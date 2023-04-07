# imports
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_`%(constraint_name)s`",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
})

db = SQLAlchemy(metadata=metadata)


class Team(db.Model, SerializerMixin):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    city = db.Column(db.String, nullable=False)
    sport = db.Column(db.String, nullable=False)
    founding_year = db.Column(db.Integer)
    # player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    # players = db.relationship("Player", backref="teams")
    serialze_rules = ('-players.teams')

    @validates('sport')
    def check_sport(self, key, value):
        validate_sport = ["baseball", "football",
                          "soccer", "hockey", "basketball"]
        if value in validate_sport:
            return value
        else:
            raise Exception("Not valid sport")

    @validates('name', 'city')
    def check_length(self, key, value):
        if len(value) >= 2:
            return value
        else:
            raise Exception("Not valid entry")

    @validates('founding_year')
    def check_length(self, key, value):
        if 1900 <= value <= 2023:
            return value
        else:
            raise Exception("Please enter year as a four digit value")

class Manager(db.Model, SerializerMixin):
    __tablename__ = 'managers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    # player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    players = db.relationship("Player", backref='managers')
    serialize_rules = ('-players.managers')

    @validates('name')
    def check_length(self, key, value):
        if len(value) >= 2:
            return value
        else:
            raise Exception("Not valid entry")

class Player(db.Model, SerializerMixin):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    salary = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    # team = db.relationship("Team", backref = "players")
    manager_id = db.Column(db.Integer, db.ForeignKey('managers.id'))
    # manager = db.relationship("Manager", backref = "players")
    serialize_rules = ('-managers.players', '-teams.players')

    @validates('salary')
    def check_salary(self, key, value):
        if value >= 0:
            return value
        else:
            raise Exception("Not a valid salary")

    @validates('name')
    def check_length(self, key, value):
        if len(value) >= 2:
            return value
        else:
            raise Exception("Not valid entry")

    # team = db.relationship("Team", backref = "players")
    # serialize_rules = ('-teams.players')


