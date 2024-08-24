import pandas as pd
from pandas import DataFrame, ExcelFile

WORKSHEET_PROMPT = "Choose worksheet:"
FILE_PATH_PROMPT = "What's the path to the IDT Spreadsheet? "
FILE_ERROR_PROMPT = "Unable to open file! Try again"
INVALID_WORKSHEET_PROMPT = "Sorry that isn't a valid selection! Try again"


def main():
    print("Hello")

    opened_excel_file = False
    while not opened_excel_file:
        idt_path = input(FILE_PATH_PROMPT)
        try:
            idt_file = pd.ExcelFile(idt_path)
            opened_excel_file = True
        except:
            print(FILE_ERROR_PROMPT)

    idt_sheets = idt_file.sheet_names
    selected_valid_sheet = False
    while not selected_valid_sheet:
        print(WORKSHEET_PROMPT)
        for i in range(len(idt_sheets)):
            print(f"\t{i}. {idt_sheets[i]}")

        user_selection = int(input())
        if user_selection >= 0 and user_selection < len(idt_sheets):
            selected_valid_sheet = True
        else:
            print(INVALID_WORKSHEET_PROMPT)

    selected_sheet = idt_sheets[user_selection]
    gold_idt = idt_file.parse(selected_sheet, header=None)

    gold_idt_columns = gold_idt.columns
    for column in gold_idt_columns:
        if column % 2 == 0:
            print(gold_idt[column])


if __name__ == "__main__":
    main()
