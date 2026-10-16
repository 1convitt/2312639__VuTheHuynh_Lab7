class GPSSignalLostError(Exception):
    """Raised when the device loses its GPS signal."""


def get_current_location():
    """Simulate a GPS hardware call; replace with a mock in unit tests."""
    return (10.0, 105.0)
