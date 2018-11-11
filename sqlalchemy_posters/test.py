#!/usr/bin/env python3
# encoding: utf-8

import os
import sys
from sqlalchemy import (
	Column,
	Date,
	FetchedValue,
	Float,
	ForeignKey,
	Integer,
	Text,
	String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Poster(Base):
	__tablename__ = 'poster'

	id = Column(Integer, primary_key=True)
	title = Column(String(280), nullable=False)
	location = Column(String(128), nullable=False)
	lat = Column(Float, FetchedValue(), nullable=False)
	long = Column(Float, FetchedValue(), nullable=False)
	text = Column(Text, nullable=True)
	author = Column(String(128), nullable=False)
	date = Column(Date, FetchedValue(), nullable=False)
	last_modified = Column(Date, FetchedValue(), nullable=True)


engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.create_all(engine)
