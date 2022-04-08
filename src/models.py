from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites_characters = db.relationship('UserFavoriteCharacter', backref="user")
    favorites_planets = db.relationship('UserFavoritePlanet', backref="user")
    favorites_starships = db.relationship('UserFavoriteStarship', backref="user")
    
    def __repr__(self):
        return '<User %r>' % self.user_name

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            "password": self.password,
            "is_active": self.is_active,
            "favorites_characters": self.favorites_characters,
            "favorites_planets": self.favorites_planets,
            "favorites_starships": self.favorites_starships
            # do not serialize the password, its a security breach

        }
    
class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    birth = db.Column(db.String(250), nullable=False)
    species = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    mass = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    home_world = db.Column(db.String(250), nullable=False)
    favorites_characters = db.relationship('UserFavoriteCharacter', backref="character")

    
    def __repr__(self):
        return '<User %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth": self.birth,
            "species": self.species,
            "height": self.height,
            "mass": self.mass,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "home_world": self.home_world,
            "favorites_characters": self.favorites_characters

        }

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    rotation_period = db.Column(db.String(250), nullable=False)
    orbital_period = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    favorites_planets = db.relationship('UserFavoritePlanet', backref="planet")
    
    
    def __repr__(self):
        return '<User %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "climate": self.climate,
            "favorites_planets": self.favorites_planets
            
        }

class Starship(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    manufacture = db.Column(db.String(250), nullable=False)
    class_type = db.Column(db.String(250), nullable=False)
    speed = db.Column(db.String(250), nullable=False)
    cost = db.Column(db.String(250), nullable=False)
    hyperdrive_rating = db.Column(db.String(250), nullable=False)
    mglt = db.Column(db.String(250), nullable=False)
    lenght = db.Column(db.String(250), nullable=False)
    cargo_capacity = db.Column(db.String(250), nullable=False)
    minimum_crew = db.Column(db.String(250), nullable=False)
    passanger = db.Column(db.String(250), nullable=False)
    favorites_starships = db.relationship('UserFavoriteStarship', backref="starship")
    
    def __repr__(self):
        return '<User %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacture": self.manufacture,
            "class_type": self.class_type,
            "speed": self.speed,
            "cost": self.cost,
            "hyperdrive_rating": self.hyperdrive_rating,
            "mglt": self.mglt,
            "lenght": self.lenght,
            "cargo_capacity": self.cargo_capacity,
            "minimum_crew": self.minimum_crew,
            "passanger": self.passanger,
            "favorites_starships": self.favorites_starships
        }

class UserFavoriteCharacter(db.Model):
    __tablename__ = 'users_favorites_characters'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))

    def __repr__(self):
        return '<User %r>' % self.user_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "characters_id": self.characters_id
        }

class UserFavoritePlanet(db.Model):
    __tablename__ = 'users_favorites_planets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))

    def __repr__(self):
        return '<UserFavoritesPlanets %r>' % self.user_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets_id": self.planets_id
        }

class UserFavoriteStarship(db.Model):
    __tablename__ = 'users_favorites_starships'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    starships_id = db.Column(db.Integer, db.ForeignKey('starships.id'))

    def __repr__(self):
        return '<User %r>' % self.username
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "starships_id": self.starships_id
        }
