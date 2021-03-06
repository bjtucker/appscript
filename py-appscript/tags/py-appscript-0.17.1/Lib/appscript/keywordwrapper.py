"""keywordwrapper -- generic wrapper for application-specific type and enum names.

(C) 2004 HAS"""

# The Keyword class provides a generic wrapper for class, enum, property and type names.
# Users don't instantiate this class directly; instead, the syntactic sugar layer allows keywords
# to be created by referring to the exported 'k' variable; e.g. k.document, k.ask, k.name, k.String.

class Keyword:
	"""A class/property/enumerator/type name."""
	
	def __init__(self, name): 
		self.AS_name = name
	
	def __repr__(self): 
		return 'k.%s' % self.AS_name
	
	def __hash__(self): 
		return hash(self.AS_name)
	
	def __eq__(self, val):
		return val.__class__ == self.__class__ and val.AS_name == self.AS_name
	
	def __ne__(self, val):
		return not self.__eq__(val)
	
	def __nonzero__(self):
		return self.AS_name != 'MissingValue'
	
	name = property(lambda self:self.AS_name)


class _KeywordShim:
	# used to fake an infinitely large namespace
	def __getattr__(self, name): return Keyword(name)


k = _KeywordShim()

