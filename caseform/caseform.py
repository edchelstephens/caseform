from inflection import camelize, underscore

from config.settings import TRANSFORM_CALLABLES
from config.messages import invalid_transform_message

def transform(mapping, func, *args, **kwargs):
	"""Returns a transformed case mapping via case transformation func callable."""
	try:	
		if func not in TRANSFORM_CALLABLES:
			raise ValueError(invalid_transform_message())

		_mapping = dict()
		
		for key, value in mapping.items():
			trans_key = func(key, *args, **kwargs)			
			_mapping[trans_key] = value

		return _mapping

	except Exception as exc:
		raise exc

def camelform(mapping, uppercase_first_letter=False):
	"""Transform a mapping object to it's equivalent camelcase keyed mapping."""
	return transform(mapping, camelize, uppercase_first_letter)

def snakeform(mapping):
	"""Transforms a mapping object to it's equivalent snakecase keyed mapping"""
	return transform(mapping, underscore)


