from typing import Dict, List

import pandas as pd

import Patient

"""
#TODO: implementation
    receive path to excel file from controller
    create pandas ExcelFile
    return list of worksheets inside the file to the controller
    parse the ExcelFile into pandas DataFrame(s) and then into Patient objects
    give controller the Patient objects for the given IDT date
    update the actual excel file whenever edits are made
    export list of Patient objects into a word document
"""


class Model:
    IDT_EXCEL_FILE: pd.ExcelFile  # for getting info FROM the file
    EXCEL_WRITER: pd.ExcelWriter  # for saving info TO the file
    patient_dict: Dict[
        str, List[Patient]]  # key is the date, value is list of all patients for that date

    # todo
    def __init__(self, file_path: str):
        self.IDT_EXCEL_FILE = None  # FIXME
        self.EXCEL_WRITER = None  # FIXME
        self.patient_dict = self.__parse_excel__()

    # TODO
    def __parse_excel__(self) -> Dict[str, List[Patient]]:
        """
        helper to parse the excel file into a list of patients for every tab/date, and to then put those lists into a
        dictionary where the tab name/date is the key
        @return: dictionary with all the patient info from the excel file
        """
        excel_file = self.IDT_EXCEL_FILE  # if excel_file == None then throw error?
        patient_dict = {}

        for date in self.get_date_options():
            curr_patients = self.__create_patient_list(date, excel_file[date])  # get list of patients from this date
            patient_dict[date] = curr_patients  # add curr patients to dictionary using date as key

        return patient_dict

    # TODO
    def __create_patient_list(self, date: str, date_sheet: pd.DataFrame) -> List[Patient]:
        """
        helper to create list of patients from a given date (aka given tab in the excel file)
        @param date: str name of the tab/date we're getting the patients from
        @param date_sheet: pd.DataFrame containing the excel info for the given date
        @return: list of all the patients from the given date
        """
        pass

    # TODO
    def __create_patient__(self, patient_info: pd.DataFrame) -> Patient:
        """
        helper to parse excel sheet info into a Patient
        @param patient_info: subset of the idt excel file with info for this specific patient
        @return: Patient object with all the patient information
        """
        pass

    # todo
    def export_idt(self, date: str, file_path: str):
        """
        export all the patients from the given date into a word(or markdown??) file at the designated path
        @param date: which tab of the spreadsheet to get all the patients from
        @param file_path: path to save the exported file to
        """
        pass

    # todo
    def get_patients(self, date: str) -> [Patient]:
        """
        @param date: string for the date we want to get the patients from
        @return: list of Patient objects for the given date
        """
        pass

    def get_date_options(self) -> [str]:
        """
        @return: list of date tabs in the idt_excel_file
        """
        return self.IDT_EXCEL_FILE.sheet_names

    # TODO
    def save_date(self, date: str) -> None:
        """
        save all the patients for a given date to the excel file
        @param date: string for the date we want to get patients from
        """
        pass

    # TODO
    def __sort_patients__(self, date: str) -> None:
        """
        sort the patients alphabetically
        @param date: str for the date we're getting the patients from
        """
        pass
