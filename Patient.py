from typing import Dict
from PatientRecord import PatientRecord
from enum import Enum


class Status(Enum):
    NEW_PATIENT = 1
    DECEASED = 2
    DISCHARGED = 3
    CURRENT_PATIENT = 4  # none of the above apply


class Patient:
    records: Dict[
        str, PatientRecord
    ]  # str date as the key then patient record object as the value
    name: str
    patient_status: Status

    # TODO
    def __init__():
        pass

    # TODO
    def add_record(new_record: PatientRecord) -> None:
        pass

    # TODO
    def get_record(desired_date: str):
        pass

    # TODO
    def check_status() -> Status:
        pass

    # TODO
    def set_status() -> None:
        pass
