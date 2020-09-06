from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os 

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db') # platform independent path helper

db = SQLAlchemy(app)

@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created!')

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped!')

@app.cli.command('db_seed')
def db_seed():
    mercury = Planet(name='Mercury',
                    ptype='Class D',
                    home_star='Sol',
                    mass=3.258e23,
                    radius=1516,
                    distance=35.98e6)

    venus = Planet(name='Venus',
                    ptype='Class K',
                    home_star='Sol',
                    mass=4.867e24,
                    radius=3760,
                    distance=67.24e6)

    earth = Planet(name='Earth',
                    ptype='Class M',
                    home_star='Sol',
                    mass=3760,
                    radius=3959,
                    distance=92.96e6)
    
    db.session.add(mercury)
    db.session.add(venus)
    db.session.add(earth)
    db.session.commit()
    print('Database seeded!')

    test_user = User(
                first_name='James', 
                last_name='McCarthy', 
                email='test@test.com', 
                password='password123')
    db.session.add(test_user)
    db.session.commit()



@app.route('/')
def index():
    return jsonify(message='Hello World!')

@app.route('/test')
def test():
    return 'Hello from the Planetary API.'

@app.route('/params')
def params():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message = 'Sorry ' + name + ', you are not old enough.'), 401
    else:
        return jsonify(message = 'Welcome ' + name + '.')

@app.route('/dynamic_url/<string:name>/<int:age>')
def dynamic_url(name: str, age: int):
    if age < 18:
        return jsonify(message = 'Sorry ' + name + ', you are not old enough.'), 401
    else:
        return jsonify(message = 'Welcome ' + name + '.')

@app.route('/not_found')
def not_found():
    return jsonify(message='That resource was not found'), 404



# models

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

class Planet(db.Model):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ptype = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)
