# Joey Velez-Ginorio
# --------------------------------
# Object Implementation for OOMDP
# --------------------------------

class Object(object):
	"""
		Formally defines an object for an OOMDP. Specifies class membership,
		and attributes with their values and domain. In addition, the __hash__
		method is implemented to efficiently retrieve the object state, via a 
		bit string of "terms" as specified in (Diuk et al., 2008). 
	"""

	def __init__(self, name, c, att):
		"""
			Initializes class membership of object, and the attributes with
			their respective values and domains.

			Params:
				c -> is a string denoting class membership, e.g. 'Taxi'
				att -> is a dict mapping attributes to their values, 
					e.g. {'Location':(1,2)}
		"""

		self.name = name
		self.c = c
		self.att = att


	def __str__(self):
		"""
			Returns the current state of the world i.e. terms tied to object.
		"""

		terms = \
		[{att:self.att[att]} for att in self.att if type(self.att[att])==bool]

		return ''.join([str(int(t.values()[0])) for t in terms])

	def state(self):
		"""
			Returns the current state of the world in string format.
		"""

		return str(self)
		
		