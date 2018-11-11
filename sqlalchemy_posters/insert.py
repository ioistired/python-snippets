#!/usr/bin/env python3
# encoding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from test import Base, Poster


engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine

DBSession = sessionmaker(engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

new_poster = Poster(
	title='stinky apartment',
	text="it sucks don't rent",
	location='MSV, Chicago, IL, US',
	author='Ben',
)
session.add(new_poster)
session.commit()
