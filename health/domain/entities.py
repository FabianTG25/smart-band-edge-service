"""Domain Entities for Health Modules"""

from datetime import datetime

class HealthRecord:
    """Represents a health record entity in the Health context.
    Attributes:
        id (int): Unique identifier for the health record.
        device_id (str): Identifier for the device that recorded the health data.
        bpm (float): Beats per minute recorded by the device.
        created_at (datetime): Timestamp when the record was created.
    """
    
    def __init__(self, device_id: str, bpm: float, created_at:datetime, id: int):
        """Intializes a HealthRecord instance.
        Args:
            device_id (str): Identifier for the device that recorded the health data.
            bpm (float): Beats per minute recorded by the device.
            created_at (datetime): Timestamp when the record was created.
            id (int): Unique identifier for the health record.
        """
        self.id = id
        self.device_id = device_id
        self.bpm = bpm
        self.created_at = created_at