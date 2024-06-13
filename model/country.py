#!/usr/bin/python3
"""countrie."""

import uuid
from datetime import datetime


class Country:
    """Class """
    def __init__(self, name):
        # Generate a UUID4 for unique identification
        self.name = name
        self.country_id = str(uuid.uuid4())
        self.created_at = datetime.now()  # Record creation timestamp
        self.updated_at = datetime.now()  # Record update timestamp

    def to_dict(self):
        """Returns  country """
        return {
            'country_id': self.country_id,
            'name': self.name,
            # Convert datetime to ISO 8601 format
            'created_at': self.created_at.isoformat(),
            # Convert datetime to ISO 8601 format
            'updated_at': self.updated_at.isoformat()
        }