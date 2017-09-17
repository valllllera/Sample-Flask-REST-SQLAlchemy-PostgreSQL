from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
    

class SportSpot(Base):

    __tablename__ = 'sport_spots'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    address = Column(String(200))

    def __repr__(self):
        return '<Spot %r>' % self.title


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from settings import DB_URI
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
