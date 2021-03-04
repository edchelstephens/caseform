from inflection import camelize, underscore

TRANSFORM_NAMES = ["camelize", "underscore"]
TRANSFORM_CALLABLES = [camelize, underscore]


def invalid_transform_message():
	"""Return invalid transform argument message."""
	message = "transform argument not in "
	for name in TRANSFORM_NAMES:
		message += "{} ".format(name)
	return message

def transform(mapping, transform, *args, **kwargs):
	"""Transform mapping to specified key case transformation."""
	try:	
		if transform not in TRANSFORM_CALLABLES:
			raise ValueError(invalid_transform_message())

		_mapping = dict()
		for key, value in mapping.items():
			trans_key = transform(key, *args, **kwargs)
			_mapping[trans_key] = value
		mapping = _mapping

	except Exception as exc:
		raise exc

def camelform(mapping, uppercase_first_letter=False):
	"""Transform a mapping object to it's equivalent camelcase keyed mapping."""
	transform(mapping, camelize, uppercase_first_letter)

def snakeform(mapping):
	"""Transforms a mapping object to it's equivalent snakecase keyed mapping"""
	transform(mapping, underscore)


