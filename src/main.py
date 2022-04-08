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
from models import db, Character
from models import db, Planet
from models import db, Starship
from models import db, UserFavoriteCharacter
from models import db, UserFavoritePlanet
from models import db, UserFavoriteStarship
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

#------------------------------------------------------------ USER --------------------------------------------------------------#

@app.route('/users', methods=['GET', 'POST'])
def create_user():
    
    if request.method == 'GET':
        users = User.query.all()
        users = list(map(lambda user: user.serialize(), users))

        return jsonify(users), 200

    if request.method == 'POST':
        user_name = request.json.get('user_name')
        email = request.json.get('email')
        password = request.json.get('password')
        is_active = request.json.get('is_active')
        
        if not user_name: return jsonify({"message": "user_name is required!"}), 400
        if not email: return jsonify({"message": "email is required!"}), 400
        if not password: return jsonify({"message": "password is required!"}), 400
        if not is_active: return jsonify({"message": "is_active is required!"}), 400
           
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
        user = User(user_name=user_name, email=email, password=password, is_active=True)

        db.session.add(user)
        db.session.commit()     
        
        return jsonify(user.serialize()), 201

#------------------------------------------------------------ CHARACTERS --------------------------------------------------------------#

@app.route('/characters', methods=['GET', 'POST'])
def create_characters():

    if request.method == 'GET':
        characters = Character.query.all()
        characters = list(map(lambda character: character.serialize(), characters))

        return jsonify(characters), 200

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

        if not name: return jsonify({"message": "name is required!"}), 400
        if not birth: return jsonify({"message": "birth is required!"}), 400
        if not species: return jsonify({"message": "species is required!"}), 400
        if not height: return jsonify({"message": "height is required!"}), 400
        if not mass: return jsonify({"message": "mass is required!"}), 400
        if not gender: return jsonify({"message": "gender is required!"}), 400
        if not hair_color: return jsonify({"message": "hair_color is required!"}), 400
        if not skin_color: return jsonify({"message": "skin_color is required!"}), 400
        if not home_world: return jsonify({"message": "home_world is required!"}), 400
           
        characters = Character()
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

@app.route('/characters/<int:characters_id>', methods=['GET'])
def get_one_character(characters_id):

    characters = Character.query.get(characters_id)
    return jsonify(characters.serialize()), 200

#------------------------------------------------------------ PLANETS --------------------------------------------------------------#

@app.route('/planets', methods=['GET', 'POST'])
def create_planets():

    if request.method == 'GET':
        planets = Planet.query.all()
        planets = list(map(lambda planet: planet.serialize(), planets))

        return jsonify(planets), 200

    if request.method == 'POST':
        name = request.json.get('name')
        population = request.json.get('population')
        rotation_period = request.json.get('rotation_period')
        orbital_period = request.json.get('orbital_period')
        diameter = request.json.get('diameter')
        gravity = request.json.get('gravity')
        terrain = request.json.get('terrain')
        climate = request.json.get('climate')

        if not name: return jsonify({"message": "name is required!"}), 400
        if not population: return jsonify({"message": "population is required!"}), 400
        if not rotation_period: return jsonify({"message": "rotation_period is required!"}), 400
        if not orbital_period: return jsonify({"message": "orbital_period is required!"}), 400
        if not diameter: return jsonify({"message": "diameter is required!"}), 400
        if not gravity: return jsonify({"message": "gravity is required!"}), 400
        if not terrain: return jsonify({"message": "terrain is required!"}), 400
        if not climate: return jsonify({"message": "climate is required!"}), 400
           
        planets = Planet()
        planets.name = name
        planets.population = population
        planets.rotation_period = rotation_period
        planets.orbital_period = orbital_period
        planets.diameter = diameter
        planets.gravity = gravity
        planets.terrain = terrain
        planets.climate = climate

        db.session.add(planets)
        db.session.commit()     
        
        return jsonify(planets.serialize()), 201

@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_one_planet(planets_id):

    planets = Planet.query.get(planets_id)
    return jsonify(planets.serialize()), 200

#------------------------------------------------------------ STARSHIPS --------------------------------------------------------------#

@app.route('/starships', methods=['GET', 'POST'])
def create_starships():

    if request.method == 'GET':
        starships = Starship.query.all()
        starships = list(map(lambda starship: starship.serialize(), starships))

        return jsonify(starships), 200

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
        passanger = request.json.get('passanger')

        if not name: return jsonify({"message": "name is required!"}), 400
        if not model: return jsonify({"message": "model is required!"}), 400
        if not manufacture: return jsonify({"message": "manufacture is required!"}), 400
        if not class_type: return jsonify({"message": "class_type is required!"}), 400
        if not speed: return jsonify({"message": "speed is required!"}), 400
        if not hyperdrive_rating: return jsonify({"message": "hyperdrive_rating is required!"}), 400
        if not mglt: return jsonify({"message": "mglt is required!"}), 400
        if not cost: return jsonify({"message": "cost is required!"}), 400
        if not lenght: return jsonify({"message": "lenght is required!"}), 400
        if not cargo_capacity: return jsonify({"message": "cargo_capacity is required!"}), 400
        if not minimum_crew: return jsonify({"message": "minimum_crew is required!"}), 400
        if not passanger: return jsonify({"message": "passanger is required!"}), 400
           
        starships = Starship()
        starships.name = name
        starships.model = model
        starships.manufacture = manufacture
        starships.class_type = class_type
        starships.speed = speed
        starships.cost = cost
        starships.hyperdrive_rating = hyperdrive_rating
        starships.mglt = mglt
        starships.lenght = lenght
        starships.cargo_capacity = cargo_capacity
        starships.minimum_crew = minimum_crew
        starships.passanger = passanger
           
        db.session.add(starships)
        db.session.commit()     
        
        return jsonify(starships.serialize()), 201

@app.route('/starships/<int:starships_id>', methods=['GET'])
def get_one_starship(starships_id):

    starships = Starship.query.get(starships_id)
    return jsonify(starships.serialize()), 200

#------------------------------------------------------------ USER FAVORTIES --------------------------------------------------------------#

@app.route('/user/<int:user_id>/favorites', methods=['GET'])
def get_all_user_favorites(user_id):
    if user_id is not None:
        usersID = User.query.get(user_id)
        users_favorites_characters = UserFavoriteCharacter.query.all()
        users_favorites_characters = list(map(lambda x: x.serialize(), users_favorites_characters))

        users_favorites_planets = UserFavoritePlanet.query.all()
        users_favorites_planets = list(map(lambda x: x.serialize(), users_favorites_planets))

        users_favorites_starships = UserFavoriteStarship.query.all()
        users_favorites_starships = list(map(lambda x: x.serialize(), users_favorites_starships))

        return jsonify(users_favorites_characters, users_favorites_planets, users_favorites_starships), 200


#------------------------------------------------------------ USER FAVORTIES CHARACTERS  --------------------------------------------------------------#

@app.route('/user/<int:user_id>/favorite/character/<int:characters_id>', methods=['POST', 'DELETE'])
def user_favorites_characters(user_id, characters_id):

    if request.method == 'POST':
        if user_id is not None and characters_id is not None:
            favorites_characters = UserFavoriteCharacter()
            favorites_characters.user_id = user_id
            favorites_characters.characters_id = characters_id

            db.session.add(favorites_characters)
            db.session.commit()     
            
            return jsonify(favorites_characters.serialize()), 201

    if request.method == 'DELETE':
        if user_id is not None and characters_id is not None:
            favorites_characters = UserFavoriteCharacter()
            db.session.delete(favorites_characters)
            db.session.commit()     
            
            return jsonify(favorites_characters.serialize()), 200

#------------------------------------------------------------ USER FAVORTIES PLANETS --------------------------------------------------------------#

@app.route('/user/<int:user_id>/favorite/planet/<int:planets_id>', methods=['POST', 'DELETE'])
def user_favorites_planets(user_id, planets_id):
      
    if request.method == 'POST':
        if planets_id is not None:
            favorites_planets = UserFavoritePlanet()
            favorites_planets.user_id = user_id
            favorites_planets.planets_id = planets_id

            db.session.add(favorites_planets)
            db.session.commit()     
        
            return jsonify(favorites_planets.serialize()), 201

    if request.method == 'DELETE':
        if planets_id is not None:
            favorites_planets = UserFavoritePlanet()
            db.session.delete(favorites_planets)
            db.session.commit()     
            
            return jsonify(favorites_planets.serialize()), 200

#------------------------------------------------------------ USER FAVORTIES STARSHIPS  --------------------------------------------------------------#

@app.route('/user/<int:user_id>/favorite/starship/<int:starships_id>', methods=['POST', 'DELETE'])
def user_favorites_starships(user_id, starships_id):

    if request.method == 'POST':
        if starships_id is not None:
            favorites_starships = UserFavoriteStarship()
            favorites_starships.user_id = user_id
            favorites_starships.starships_id = starships_id

            db.session.add(favorites_starships)
            db.session.commit()     
        
            return jsonify(favorites_starships.serialize()), 201

    if request.method == 'DELETE':
        if starships_id is not None:
            favorites_starships = UserFavoritePlanet()
            db.session.delete(favorites_starships)
            db.session.commit()     
            
            return jsonify(favorites_starships.serialize()), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
