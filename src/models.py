from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    # def __repr__(self):
    #     return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }
        
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email
        }

class UserFavoritesPlanets(db.Model):
    __tablename__ = 'userFavoritesPlanets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planets = db.relationship('Planets')

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user": self.user,
            "planets_id": self.planets_id,
            "planets": self.planets
        }

class UserFavoritesCharacters(db.Model):
    __tablename__ = 'userFavoritesCharacters'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    characters = db.relationship('Characters')

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user": self.user,
            "characters_id": self.characters_id,
            "characters": self.characters
        }

class UserFavoritesVehicles(db.Model):
    __tablename__ = 'userFavoritesVehicles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    vehicles = db.relationship('Vehicles')

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user": self.user,
            "vehicles_id": self.vehicles_id,
            "vehicles": self.vehicles
        }

class UserFavoritesStarships(db.Model):
    __tablename__ = 'userFavoritesStarships'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    starships_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    starships = db.relationship('Starships')

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user": self.user,
            "starships_id": self.starships_id,
            "starships": self.starships
        }

class Planets(db.Model):
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

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population_period": self.population_period,
            "totation_period": self.totation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "climate": self.climate
        }
    
class Characters(db.Model):
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
            "home_world": self.home_world
        }

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    manufacture = db.Column(db.String(250), nullable=False)
    class_type = db.Column(db.String(250), nullable=False)
    speed = db.Column(db.String(250), nullable=False)
    cost = db.Column(db.String(250), nullable=False)
    lenght = db.Column(db.String(250), nullable=False)
    cargo_capacity = db.Column(db.String(250), nullable=False)
    minimum_crew = db.Column(db.String(250), nullable=False)
    passenger = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacture": self.manufacture,
            "class_type": self.class_type,
            "speed": self.speed,
            "cost": self.cost,
            "lenght": self.lenght,
            "cargo_capacity": self.cargo_capacity,
            "minimum_crew": self.minimum_crew,
            "passenger": self.passenger
        }


class Starships(db.Model):
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
            "passenger": self.passenger  
        }
    