from .settings import TRANSFORM_NAMES

def invalid_transform_message():
	"""Return invalid transform func argument message."""

	message = "transform function argument not in "
	for name in TRANSFORM_NAMES:
		message += "{} ".format(name)
	return message
