"""
#TODO: implementation
    receive path to excel file from controller
    create pandas ExcelFile
    return list of worksheets inside the file to the controller
    parse the ExcelFile into pandas DataFrame(s) and then into Patient objects
    give controller the Patient object it requests (filters?)
    update the actual excel file whenever edits are made
    export list of Patient objects into a word document

#TODO:
    figure out what controller wants to receive
        all the different Patients for a given worksheet?
        or the same Patient across worksheets?
    figure out time stuff: one worksheet per week? how does idt date change?
"""