from sqlalchemy import create_engine, MetaData, ForeignKey, Table, Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship, Session

import environs

env = environs.Env()
env.read_env()

DB_URI = env('MANGO_URI')
engine = create_engine(DB_URI, echo=True, future=True)
session = Session(engine)
metadata = MetaData()
Base = declarative_base(metadata=metadata)

# club_table = Table("club", metadata, autoload_with=engine)
# friend_table = Table("friend", metadata, autoload_with=engine)

friends_table = Table('friends_table', Base.metadata,
    Column('friends_to', Integer, ForeignKey('friend.id')),
    Column('friended_by', Integer, ForeignKey('friend.id'))
)

class Club(Base):
    # __table__ = club_table
    __tablename__ = "club"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self) -> str:
        return f"{self.name} <{self.id}>"

class Friend(Base):
    # __table__ = friend_table
    __tablename__ = "friend"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    club_id = Column(Integer, ForeignKey('club.id'))
    club = relationship('Club')


    friends = relationship(
        "Friend",
        foreign_keys="[friends_to, friended_by]",
        secondary=friends_table, 
        back_populates="friends")

    def __repr__(self) -> str:
        return f"{self.name} <{self.id}>"


# class Brother(Base):
#     __tablename__ = "brother"

#     id = Column(Integer, primary_key=True)
    

association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship(
        "Child",
        secondary=association_table,
        back_populates="parents")

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
    parents = relationship(
        "Parent",
        secondary=association_table,
        back_populates="children")

# def populate_data():
#     with Session(engine) as session:
#         club = Club(name="The Man Portugal")
#         f1 = Friend(name="Macklemore")
#         f2 = Friend(name="Vance Joy")
#         session.add(club)
#         session.add(f1)
#         session.add(f2)
#         session.commit() 
