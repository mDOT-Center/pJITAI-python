
class RLError(Exception):
    """Base class for all RL exceptions."""
    pass

class RLValidationError(RLError):
    """Raised when a validation error occurs."""
    pass
