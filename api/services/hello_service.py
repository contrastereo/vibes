from api.exceptions.api_exceptions import MissingParameterError

def get_hello_message():
    """Get the default hello message."""
    return "Hello, World!"

def get_hello_name_message(name):
    """Get a personalized hello message."""
    if not name:
        raise MissingParameterError()
    return f"Hello, {name}!" 