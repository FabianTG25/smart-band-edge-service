from datetime import datetime, timezone
from dateutil.parser import parse

from health.domain.entities import HealthRecord

class HealthRecordService:
    def __init__(self):
        """Initialize the health record service.
        """
        pass
    @staticmethod
    def create_record(device_id: str, bpm: float, created_at: datetime, id: int | None) -> HealthRecord:
        """Creates a HealthRecord.
        
        Args:
            device_id (str): Identifier for the device that recorded the health data.
            bpm (float): Beats per minute recorded by the device.
            created_at (datetime): Timestamp when the record was created.
            
        Returns:
            HealthRecord: The created HealthRecord instance.
            Raises:
                ValueError: If bpm is not a valid float or out of range (0-200).
                ValueError: If created_at is not a valid datetime string.
        """

        try:
            bpm = float(bpm)
            if not (0<= bpm <= 200):
                raise ValueError("Invalid BPM value")
            if created_at:
                parse_created_at = parse(created_at).astimezone(timezone.utc)
            else :
                parse_created_at = datetime.now(timezone.utc)
        except (ValueError, TypeError) :
            raise ValueError("Invalid data format")

        return HealthRecord(device_id, bpm, created_at, id)