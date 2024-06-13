#!/usr/bin/python3
"""  cities"""

import uuid
from datetime import datetime


class City:
    """Classcity."""

    def __init__(self, name, country_id):
        # Generate a UUID4 for unique identification
        self.city_id = str(uuid.uuid4())
        self.name = name
        self.country_id = country_id
        self.created_at = datetime.now()  # Record creation timestamp
        self.updated_at = datetime.now()  # Record update timestamp

    def to_dict(self):
        """Return city """
        return {
            'city_id': self.city_id,
            'name': self.name,
            'country_id': self.country_id,
            # Convert datetime to ISO 8601 format
            'created_at': self.created_at.isoformat(),
            # Convert datetime to ISO 8601 format
            'updated_at': self.updated_at.isoformat()
        }