import datetime as dt


class Patient:
    #FIXME: rename some fields and maybe add some fields
    name: str
    idt_date: dt.date
    need_recertification: bool
    dc: bool
    passed: bool
    medication_plan: str
    care_plan: str
    poc_change_requests: str
    assessment_comments: str
    poc_followup: str

    def __init__(self) -> None:
        pass

    def __str__(self):
        return super().__str__()

    def get_idt_date(self) -> dt.date:
        return self.idt_date

    def set_idt_date(self, new_date: dt.date) -> None:
        self.idt_date = new_date

    def get_recertification_status(self) -> bool:
        return self.need_recertification

    def set_recertification_status(self, new_recert: bool) -> None:
        self.need_recertification = new_recert

    def get_dc(self) -> bool:
        return self.dc

    def set_dc(self, new_dc: bool) -> None:
        self.dc = new_dc

    def get_passed(self) -> bool:
        return self.passed

    def set_passed(self, new_passed: bool) -> None:
        self.passed = new_passed

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
