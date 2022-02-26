"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from models import db, UserFavoritesPlanets
from models import db, UserFavoritesCharacters
from models import db, UserFavoritesVehicles
from models import db, UserFavoritesStarships
from models import db, Planets
from models import db, Characters
from models import db, Vehicles
from models import db, Starships
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# @app.route('/user', methods=['GET'])
# def handle_hello():

#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#     }

#     return jsonify(response_body), 200

# @app.route('/users', methods=['GET'])
# def table_user():
#     users = User.query.all()
#     users = list(map(lambda user: user.serialize(), users))
#     return jsonify(users), 200

@app.route('/users', methods=['POST', 'GET'])
def create_user():
    if request.method == 'POST':
        user_name = request.json.get('user_name')
        email = request.json.get('email')
           
        """
        body = request.get_json()
        user= User()
        user.user_name = body['user_name']
        user.email = body['email'] 
        """   
        """
        user= User()
        user.user_name = user_name
        user.email = email  
        """
        user = User(user_name=user_name, email=email)

        db.session.add(user)
        db.session.commit()     
        
        return jsonify(user.serialize()), 201

    else: 
        users = User.query.all()
        users = list(map(lambda user: user.serialize(), users))

        return jsonify(users), 200

@app.route('/planets', methods=['POST', 'GET'])
def create_planets():
    if request.method == 'POST':
        name = request.json.get('name')
        population = request.json.get('population')
        rotation_period = request.json.get('rotation_period')
        orbital_period = request.json.get('orbital_period')
        diameter = request.json.get('diameter')
        gravity = request.json.get('gravity')
        terrain = request.json.get('terrain')
        climate = request.json.get('climate')
        
        planets = Planets()
        Planets.name = name
        Planets.population = population
        Planets.rotation_period = rotation_period
        Planets.orbital_period = orbital_period
        Planets.diameter = diameter
        Planets.gravity = gravity
        Planets.terrain = terrain
        Planets.climate = climate

        db.session.add(planets)
        db.session.commit()     
        
        return jsonify(planets.serialize()), 201

    else: 
        planets = Planets.query.all()
        planets = list(map(lambda planet: planet.serialize(), planets))

        return jsonify(planets), 200

@app.route('/characters', methods=['POST', 'GET'])
def create_characters():
    if request.method == 'POST':
        name = request.json.get('name')
        birth = request.json.get('birth')
        species = request.json.get('species')
        height = request.json.get('height')
        mass = request.json.get('mass')
        gender = request.json.get('gender')
        hair_color = request.json.get('hair_color')
        skin_color = request.json.get('skin_color')
        home_world = request.json.get('home_world')
           
        characters = Characters()
        characters.name = name
        characters.birth = birth
        characters.species = species
        characters.height = height
        characters.mass = mass
        characters.gender = gender
        characters.hair_color = hair_color
        characters.skin_color = skin_color
        characters.home_world = home_world

        db.session.add(characters)
        db.session.commit()     
        
        return jsonify(characters.serialize()), 201

    else: 
        characters = Characters.query.all()
        characters = list(map(lambda character: character.serialize(), characters))

        return jsonify(characters), 200

@app.route('/vehicles', methods=['POST', 'GET'])
def create_vehicles():
    if request.method == 'POST':
        name = request.json.get('name')
        model = request.json.get('model')
        manufacture = request.json.get('manufacture')
        class_type = request.json.get('class_type')
        speed = request.json.get('speed')
        cost = request.json.get('cost')
        lenght = request.json.get('lenght')
        cargo_capacity = request.json.get('cargo_capacity')
        minimum_crew = request.json.get('minimum_crew')
        passenger = request.json.get('passenger')
           
        vehicles = Vehicles()
        vehicles.name = name
        vehicles.model = model
        vehicles.manufacture = manufacture
        vehicles.class_type = class_type
        vehicles.speed = speed
        vehicles.cost = cost
        vehicles.lenght =lenght
        vehicles.cargo_capacity = cargo_capacity
        vehicles.minimum_crew = minimum_crew
        vehicles.passanger = passanger

        db.session.add(vehicles)
        db.session.commit()     

        return jsonify(vehicles.serialize()), 201

    else: 
        vehicles= Vehicles.query.all()
        vehicles= list(map(lambda vehicle: vehicle.serialize(), vehicles))

        return jsonify(vehicles), 200

@app.route('/starships', methods=['POST', 'GET'])
def create_starships():
    if request.method == 'POST':
        name = request.json.get('name')
        model = request.json.get('model')
        manufacture = request.json.get('manufacture')
        class_type = request.json.get('class_type')
        speed = request.json.get('speed')
        hyperdrive_rating = request.json.get('hyperdrive_rating')
        mglt = request.json.get('mglt')
        cost = request.json.get('cost')
        lenght = request.json.get('lenght')
        cargo_capacity = request.json.get('cargo_capacity')
        minimum_crew = request.json.get('minimum_crew')
        passenger = request.json.get('passenger')
           
        starships = Starships()
        starships.name = name
        starships.model = model
        starships.manufacture = manufacture
        starships.class_type = class_type
        starships.speed = speed
        starships.cost = cost
        starships.hyperdrive_rating = hyperdrive_rating
        starships.mglt = mglt
        starships.lenght =lenght
        starships.cargo_capacity = cargo_capacity
        starships.minimum_crew = minimum_crew
        starships.passanger = passanger
           
        db.session.add(starships)
        db.session.commit()     
        
        return jsonify(starships.serialize()), 201

    else: 
        starships= Starships.query.all()
        starships= list(map(lambda starship: starship.serialize(), starships))

        return jsonify(starships), 200

@app.route('/userfavoritesplanets', methods=['POST', 'GET'])
def create_userfavoritesplanets():
    if request.method == 'POST':
        user_id = request.json.get('user_id')
        user = request.json.get('user')
        planets_id = request.json.get('planets_id')
        planets = request.json.get('planets')
             
        favorites_planets= UserFavoritesPlanets()
        favorites_Planets.user = user
        favorites_Planets.user_id = user_id
        favorites_Planets.planets = planets

        db.session.add(favorites_planets)
        db.session.commit()     
        
        return jsonify(favorites_planets.serialize()), 201

    else: 
        favorites_planets= UserFavoritesPlanets.query.all()
        favorites_planets= list(map(lambda favorites_planets: favorites_planets.serialize(), favorites_planets))

        return jsonify(favorites_planets), 200

@app.route('/userfavoritescharacters', methods=['POST', 'GET'])
def create_userfavoritescharacters():
    if request.method == 'POST':
        user_id = request.json.get('user_id')
        user = request.json.get('user')
        characters_id = request.json.get('characters_id')
        characters = request.json.get('characters')
           
        favorites_characters= UserFavoritesCharacters()
        favorites_characters.user = user
        favorites_characters.user_id = user_id
        favorites_characters.characters = characters

        db.session.add(favorites_characters)
        db.session.commit()     
        
        return jsonify(favorites_characters.serialize()), 201

    else: 
        favorites_characters= UserFavoritesPlanets.query.all()
        favorites_characters= list(map(lambda favorites_characters: favorites_characters.serialize(), favorites_characters))

        return jsonify(favorites_characters), 200

@app.route('/userfavoritesvehicles', methods=['POST', 'GET'])
def create_userfavoritesvehicles():
    if request.method == 'POST':
        user_id = request.json.get('user_id')
        user = request.json.get('user')
        vehicles_id = request.json.get('vehicles_id')
        vehicles = request.json.get('vehicles')

        favorites_vehicles= UserFavoritesVehicles()
        favorites_vehicles.user = user
        favorites_vehicles.user_id = user_id
        favorites_vehicles.vehicles = vehicles


        db.session.add(favorites_vehicles)
        db.session.commit()     
        
        return jsonify(favorites_vehicles.serialize()), 201

    else: 
        favorites_vehicles= UserFavoritesVehicles.query.all()
        favorites_vehicles= list(map(lambda favorites_vehicles: favorites_vehicles.serialize(), favorites_vehicles))

        return jsonify(favorites_vehicles), 200

@app.route('/userfavoritesstarships', methods=['POST', 'GET'])
def create_userfavoritesstarships():
    if request.method == 'POST':
        user_id = request.json.get('user_id')
        user = request.json.get('user')
        starships_id = request.json.get('starships_id')
        starships = request.json.get('starships')

        favorites_starships= UserFavoritesStarships()
        favorites_starships.user = user
        favorites_starships.user_id = user_id
        favorites_starships.starships = starships


        db.session.add(favorites_starships)
        db.session.commit()     
        
        return jsonify(favorites_starships.serialize()), 201

    else: 
        favorites_starships= UserFavoritesStarships.query.all()
        favorites_starships= list(map(lambda favorites_starships: favorites_starships.serialize(), favorites_starships))

        return jsonify(favorites_starships), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
