import datetime as dt


# FIXME: maybe don't have date and just store date as string?
# then might need to add booleans for recert, d/c and passed fields??

class Patient:
    name: str
    idt_date: dt.date
    recertification_date: dt.date  # date the next recert is due
    discharge_date: dt.date  # date they're scheduled for discharge, otherwise NULL
    date_of_passing: dt.date  # date the patient passed, otherwise NULL
    medication_plan: str
    care_plan: str
    poc_change_requests: str
    assessment_comments: str
    poc_followup: str

    # TODO
    def __init__(self) -> None:
        pass

    # TODO: either make this just for debugging or make string for export
    def __str__(self):
        return super().__str__()

    # TODO return true if recertification date is within 2 weeks of IDT date
    def recert_within_two_weeks(self) -> bool:
        return False

    # TODO return true if discharge_date exists
    def scheduled_for_discharge(self) -> bool:
        return False

    # TODO return true if date_of_passing exists
    def has_passed(self) -> bool:
        return False

    def get_idt_date(self) -> dt.date:
        return self.idt_date

    def set_idt_date(self, new_date: dt.date) -> None:
        self.idt_date = new_date

    def get_recertification_date(self) -> dt.date:
        return self.recertification_date

    def set_recertification_date(self, new_recert: dt.date) -> None:
        self.recertification_date = new_recert

    def get_discharge_date(self) -> dt.date:
        return self.discharge_date

    def set_discharge_date(self, new_dc: dt.date) -> None:
        self.discharge_date = new_dc

    def get_date_of_passing(self) -> dt.date:
        return self.date_of_passing

    def set_date_of_passing(self, new_passed: dt.date) -> None:
        self.date_of_passing = new_passed

    def get_medication_plan(self) -> str:
        return self.medication_plan

    def set_medication_plan(self, new_medication_plan: str) -> None:
        self.medication_plan = new_medication_plan

    def get_care_plan(self) -> str:
        return self.care_plan

    def set_care_plan(self, new_care_plan: str) -> None:
        self.care_plan = new_care_plan

    def get_poc_change_requests(self) -> str:
        return self.poc_change_requests

    def set_poc_change_requests(self, new_poc_change_requests: str) -> None:
        self.new_poc_change_requests = new_poc_change_requests

    def get_assessment_comments(self) -> str:
        return self.assessment_comments

    def set_assessment_comments(self, new_assessment_comments: str) -> None:
        self.assessment_comments = new_assessment_comments

    def get_poc_followup(self) -> str:
        return self.poc_followup

    def set_poc_followup(self, new_followup: str) -> None:
        self.poc_followup = new_followup

    def get_name(self) -> str:
        return self.name
