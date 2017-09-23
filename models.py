from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from passlib.apps import custom_app_context as pwd_context

from itsdangerous import (TimedJSONWebSignatureSerializer
                            as Serializer, BadSignature, SignatureExpired)

from settings import SECRET_KEY
from db import session

Base = declarative_base()
    

class SportSpot(Base):

    __tablename__ = 'spots'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    address = Column(String(200))
    author_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return '<Spot %r>' % self.title


class User(Base):
    
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    username = Column(String(32), index = True)
    password_hash = Column(String(128))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration = 60000):
        s = Serializer(SECRET_KEY, expires_in = expiration)
        return s.dumps({ 'id': self.id })

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = session.query(User).filter(User.id == data['id']).first()
        return user



if __name__ == "__main__":
    from sqlalchemy import create_engine
    from settings import DB_URI
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)




