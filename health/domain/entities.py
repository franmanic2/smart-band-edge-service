"""Domain Entities for Health Module"""
from datetime import datetime

class HealthRecord:
    """Represents a Health Record entity in the health context

    Attributes:
        id (int): The id of the Health Record
        created_at (datetime): The date and time the record was created
        device_id (str): The id of the device the record was created
        bpm (float): The BPM of the record
    """
    def __init__(self, device_id: str, bpm: float, created_at: datetime, id: int = None):
        """ Initializes a Health Record entity
        """
        self.id = id
        self.device_id = device_id
        self.created_at = created_at
        self.bpm = bpm