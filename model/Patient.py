from typing import Dict
import datetime as dt
from PatientRecord import PatientRecord
from enum import Enum


class Status(Enum):
    NEW_PATIENT = 1
    DECEASED = 2
    DISCHARGED = 3
    CURRENT_PATIENT = 4  # none of the above apply


class Patient:
    records: Dict[
        dt.date, PatientRecord
    ]  # idt date as the key then patient record object as the value
    name: str
    patient_status: Status

    def __init__(self, patient_name):
        self.name = patient_name
        self.records = {}  # empty dictionary

    def add_record(self, new_record: PatientRecord) -> None:
        key = new_record.get_idt_date()
        self.records[key] = new_record

    def get_record(self, desired_date: dt.date):
        return self.records[desired_date]

    def get_status(self) -> Status:
        return self.patient_status

    def set_status(self, new_status: Status) -> None:
        self.patient_status = new_status
