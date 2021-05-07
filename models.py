
import os

from environs import Env

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

env = Env()
env.read_env()


DB_URI = env.str('PG_URI')
engine = create_engine(DB_URI, future=True)
metadata = MetaData()
Base = declarative_base()

state_table = Table("browser_state", metadata, autoload_with=engine)
terminal_table = Table("browser_terminal", metadata, autoload_with=engine)
dest_terminal_assoc_table = Table("browser_terminal_dest_terminals", metadata, 
    # autoload_with=engine
    Column('id', Integer, primary_key=True),
    Column('from_terminal_id', Integer, ForeignKey('Terminal.id')),
    Column('to_terminal_id', Integer, ForeignKey('Terminal.id'))
    )

class State(Base):
    __table__ = state_table

    def __repr__(self):
        return f"{self.name} ({self.state_id})"

class Terminal(Base):
    __table__ = terminal_table

    state = relationship('State')
    dest_terminals = relationship('Terminal', secondary=dest_terminal_assoc_table)

    def __repr__(self) -> str:
        return f"{self.name} ({self.state_id})"

