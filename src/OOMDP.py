# Joey Velez-Ginorio
# --------------------
# OOMDP Implementation
# --------------------

import itertools
import numpy as np
from Object import Object

class OOMDP(object):
	"""
		Defines an Object-Oriented Markov Decision Process, formally defined 
		as a nine tuple, 
		< classes, attributes(c), domain(a), objects, relations, actions, transitions,
		rewards, discount >, where:

			classes -> is a set of object classes.

			attributes(c) -> is a function that specifies attributes of a 
				class c.

			domain(a) -> is a function that specifies the range of possible 
				values for an attribute a.

			objects -> is a set of objects, each of which belongs to a 
				class, C. The state of an object is a value assignment to all 
				its attributes.

			relations -> is a set of relations, specifying how two objects may
				interact. 

			actions -> is a finite set of actions.

			transitions -> specifies T(s'|s,a), probability an agent goes to s'
				by taking action a in state s. 

			rewards -> specifies R(s,a), the reward an agent receives from the 
				environment for taking action a in state s.

			discount -> is the discount factor, [0,1). The smaller lambda is, 
				the more the agent will favor immediate reward.
	"""

	def __init__(self, objects=None, relations=None, actions=None, 
				transitions=None, rewards=None, discount=None):
		"""
			Initializes parts of the nine tuple (a, t, r, lam), then
			extracts c, att(c), and dom(a) from o for the fully-defined
			OOMDP. 

			Params:
				objects -> is a 3D dict mapping objects to classes to 
				attributes.	{Object: {Class: {Attribute: Value}}}

				relations -> is a 2D dict mapping a set of classes, (c_1, c_2),
					to a list of boolean functions that operate over the set
					of classes.

				actions -> is a list of actions, e.g. [Up, Down, Left, Right]

				transitions -> is a 3D Matrix, specifiyng transition dynamics 
					from state to state, T[s'|s,a]. This can be learned through
					DOORMAX.

				rewards -> is a TBD
				
				discount -> is a discrete value [0,1), the lower it is the more 
					the agent prefers immediate reward.
		"""

		# Initialize part of the nine-tuple OOMDP, M
		self.relations = relations
		self.actions = actions
		self.transitions = transitions
		self.rewards = rewards
		self.discount = discount

		# Instantiate all instances of Object from 3D dict, O.
		updatedObjects = list()
		for obj in objects:

			# Extract object name
			temp = obj

			# Use name to create instance of Object, initialize with 
			# 	class membership, and attributes with values
			temp = Object(temp, objects[temp].keys()[0], objects[temp].values()[0])
			updatedObjects.append(temp)

		# O is now in a more accessible representation
		self.objects = updatedObjects


	def getTerms(self):
		""" 
			Retrieves all terms in the OOMDP. Terms come from all boolean 
			functions, which can be from object attributes, relations defined,
			over classes, and any boolean function defined over the state space
			that encodes prior knowledge.
		"""

		terms = ""

		# Extract terms from objects
		for o in self.objects:
			terms += o.state()

		# Extract terms from relations
		for key, val in self.relations.items():
			terms += self.checkRelations({key:val})

		# Extract terms from boolean functions encoding prior knowledge


		return terms

	def checkRelations(self, relation):
		"""
			Provided a list of boolean functions defined over classes, returns
			a string of terms corresponding to the T/F value of each relation.
		"""
		# Figure out which classes the relations are defined over
		classPair = list(relation.keys()[0])

		# Collect all objects of each class
		o1 = list()
		o2 = list()
		for o in self.objects:
			if o.c == classPair[0]:
				o1.append(o)
			if o.c == classPair[1]:
				o2.append(o)

		# Construct all object pairs that will be tested on the relation
		objectPairs = list(itertools.product(o1,o2))

		# Test all object pairs on all relations, return string of terms
		terms = ""
		for objPair in objectPairs:
			for rel in relation.values()[0]:
				terms += str(int(rel(objPair[0], objPair[1])))

		return terms













