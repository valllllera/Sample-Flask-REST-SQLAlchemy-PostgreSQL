from flask_restful import reqparse, abort, Resource, fields, marshal_with

from models import SportSpot
from models import User

from db import session



parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('address', type=str)

parser.add_argument('username', type=str)
parser.add_argument('password', type=str)



sportspot_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'address': fields.String,
}

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password_hash': fields.String,
}

class Home(Resource):
    def get(self):
        return 'Dockerized', 200


class Spot(Resource):
    @marshal_with(sportspot_fields)
    def get(self, spot_id):
        spot = session.query(SportSpot).filter(SportSpot.id == spot_id).first()
        if not spot:
            abort(404, message="Spot {} doesn't exist".format(spot_id))
        return spot

    
    def delete(self, spot_id):
        spot = session.query(SportSpot).filter(SportSpot.id == spot_id).first()
        if not spot:
            abort(404, message="Spot {} doesn't exist".format(spot_id))
        session.delete(spot)
        session.commit()
        return {}, 204


    @marshal_with(sportspot_fields)
    def put(self, spot_id):
        parsed_args = parser.parse_args()
        spot = session.query(SportSpot).filter(SportSpot.id == spot_id).first()
        spot.title = parsed_args['title']
        spot.address = parsed_args['address']
        session.add(spot)
        session.commit()
        return spot, 201


class SpotList(Resource):
    @marshal_with(sportspot_fields)
    def get(self):
        spots = session.query(SportSpot).all()
        return spots

    @marshal_with(sportspot_fields)
    def post(self):
        args = parser.parse_args()

        print(args['title'])
        s = SportSpot()
        s.title = args['title']
        s.address = args['address']

        session.add(s)
        session.commit()

        return session.query(SportSpot).order_by(SportSpot.id.desc()).first(), 201

class Register(Resource):
    @marshal_with(user_fields)
    def post(self):
        args = parser.parse_args()
        
        username = args['username']
        password = args['password']

        if username is None or password is None:
            abort(400)
        if session.query(User).filter_by(username = username).first() is not None:
            abort(404, message="User {} already exist".format(username))
            
        user = User(username = username)
        user.hash_password(password)
        session.add(user)
        session.commit()

        reged_user = session.query(User).filter(User.username == username).first()
        if not reged_user:
            abort(404, message="User {} doesn't exist".format(username))
        return reged_user
