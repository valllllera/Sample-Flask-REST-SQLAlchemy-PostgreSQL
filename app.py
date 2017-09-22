from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Api


from resources import Spot, SpotList 
from resources import Home
from resources import Register
from resources import Token
from resources import HomeAuth

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


api.add_resource(Home, '/')
api.add_resource(SpotList, '/spots')
api.add_resource(Spot, '/spots/<int:spot_id>')
api.add_resource(Register, '/register')
api.add_resource(Token, '/token')
api.add_resource(HomeAuth, '/home_auth')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
