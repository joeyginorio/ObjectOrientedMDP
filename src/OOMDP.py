# Joey Velez-Ginorio
# --------------------
# OOMDP Implementation
# --------------------

import numpy as np
from Object import Object

class OOMDP(object):
	"""
		Defines an Object-Oriented Markov Decision Process, formally defined 
		as an eight tuple, < c, att(c), dom(a), o, a, t, r, lam >, where:

			c -> is a set of object classes

			att(c) -> is a function that specifies attributes of a class c

			dom(a) -> is a function that specifies the range of possible values for
				an attribute a

			o -> is a collection of objects, each of which belonds to a class, C. 
				The state of an object is a value assignment to all its attributes.

			a -> is a finite set of actions

			t -> specifies T(s'|s,a), probability an agent goes to s' by taking 
				action a in state s. 

			r -> specifies R(s,a), the reward an agent receives from the environment
				for taking action a in state s.

			lam -> is the discount factor, [0,1). The smaller lambda is, the more 
				the agent will favor immediate reward.
	"""

	def __init__(self, o=None, a=None, t=None, r=None, lam=None):
		"""
			Initializes parts of the eight tuple (a, t, r, lam), then
			extracts c, att(c), and dom(a) from o for the fully-defined
			OOMDP. 

			Params:
				o -> is a 3D dict mapping objects to classes to attributes.
					{Object: {Class: {Attribute: Value}}}

				a -> is a list of actions, e.g. [Up, Down, Left, Right]

				t -> is a 3D Matrix, specifiyng transition dynamics from state
					to state, T[s'|s,a]. This can be learned through DOORMAX.

				r -> is a TBD
				
				lam -> is a discrete value [0,1), the lower it is the more 
					the agent prefers immediate reward.
		"""

		# Initialize part of the eight-tuple OOMDP, M
		self.o = o
		self.a = a
		self.t = t
		self.r = r
		self.lam = lam

		# Instantiate all instances of Object from 3D dict, O.
		objects = list()
		for obj in o:

			# Extract object name
			temp = obj

			# Use name to create instance of Object, initialize with 
			# 	class membership, and attributes with values
			temp = Object(o[temp].keys()[0], o[temp].values()[0])
			objects.append(temp)

		# O is now in a more accessible representation
		self.o = objects

		













