from docx import Document
from datetime import datetime
import sys
from pprint import pprint

def get_invoice_number():
    '''
    Reads the configuration document and extracts the invoice number, then iterating and returning it.
    Returns:

    Parameters
    -------
    Invoice_No: str
    The invoice number last used

    Returns
    -------
    Invoice_No: str
    '''

    Invoice_No = ''

    I_doc = Document('Invoice.docx')
    Invoice_No = str(I_doc.paragraphs[0].text)
    
    I_doc.save('Invoice.docx')

    print("Success ! Got Invoice #.")

    return Invoice_No


def set_invoice_number(Invoice_No):
    '''
    After a successful run, it takes the invoice number and writes the configuration file and replaces the old with the new.
    Returns: nothing, but perhaps a "success" note.

    Parameters
    -------
    I_doc: Document
        The open document that saves the invoice number.

    Invoice_No: str
        This is converted to int, iterated, and then saved into the file.

    Returns
    ------
    None
    '''

    I_doc = Document('Invoice.docx')
    Invoice_No = int(Invoice_No) + 1
    I_doc.paragraphs[0].text = str(Invoice_No)

    I_doc.save('Invoice.docx')
    print("Success ! Set Invoice #.")

    return None


def build_invoice(values):
    """
    Either this or the main should be the one that builds the invoice.

    Parameters
    -------
    values: dict
       {
        'C_Nam': C_Name, 'C_Tel': C_Telephone, 'C_Per': C_Person,
        'C_TRN': C_TRN, 'D_Inv': D_Invoice,
        'D': Description, 'Q': Quantity, 'U': Unit_Amount,
        'B': Base_Amount, 'V': VAT_Amount, 'T': Total_Amount
        }

    Returns
    -------
    None
    """

    doc = Document('original_file.docx')

    # Editing
    doc.paragraphs[7].text = 'Company name: ' + values['C_Nam']

    doc.tables[0].cell(0,0).text = 'TELEPHONE NO: ' + values['C_Tel']
    doc.tables[0].cell(1,0).text = 'CONTACT PERSON: ' + values['C_Per']
    doc.tables[0].cell(2,0).text = 'CUSTOMER TRN: ' + values['C_TRN']
    
    doc.tables[0].cell(0,1).text = 'INVOICE No: ' + values['D_Inv']
    doc.tables[0].cell(1,1).text = 'DATE: ' + values['Date']

    doc.tables[1].cell(1,0).text = '01'
    doc.tables[1].cell(1,1).text = '01'
    doc.tables[1].cell(1,2).text = values['D']
    doc.tables[1].cell(1,3).text = values['Q'][0]
    doc.tables[1].cell(1,4).text = values['U'][0]
    doc.tables[1].cell(1,5).text = values['U'][1]
    doc.tables[1].cell(1,6).text = values['V'][0]
    doc.tables[1].cell(1,7).text = values['V'][1]
    doc.tables[1].cell(1,8).text = values['T'][0]
    doc.tables[1].cell(1,9).text = values['T'][1]

    doc.tables[1].cell(9,8).text = 'AED: ' + values['B'][0]
    doc.tables[1].cell(9,9).text = values['B'][1]
    doc.tables[1].cell(10,8).text = 'AED: ' + values['V'][0]
    doc.tables[1].cell(10,9).text = values['V'][1]
    doc.tables[1].cell(11,8).text = 'AED: ' + values['T'][0]
    doc.tables[1].cell(11,9).text = values['T'][1]
    doc.tables[1].cell(12,0).text = values['W'] 

    doc.save(values['D_Inv'] + ' ' + values['C_Nam'] + '.docx')

    print("Success ! Created invoice !")
    
    return None


def intconvert(num):
    """
    This transforms a constant from number format to one of letters and words.

    Parameters
    ------
    num: str/int
        This comes in as str and converted into an int.
    
    numEng: dict
        This is the unique set of numbers assigned an associated english word.

    Returns
    ------
    :str
        This is the constant in word form.
    """
    numEngA =  {
		0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
		5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
		10: 'ten', 11:'eleven', 12:'twelve', 13: 'thirteen',
		14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
		17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
		}
    
    numEngB = ['twenty', 'thirty', 'fourty', 'fifty',
       'sixty', 'seventy', 'eighty', 'ninety']
    
    num = int(num)

    if 1 <= num <= 19:
	    return numEngA[num]

    elif 20 <= num <= 99:
	    tens, units = divmod(num, 10)
	    #print('The tens: {}'.format(tens))
	    #print('The units: {}'.format(units))
	    return numEngB[tens - 2] + '-' + numEngA[units] if units else numEngB[tens - 2]

    elif 100 <= num <= 999:
	    hundreds, tens = divmod(num, 100)
	    #print('The hundreds: {}'.format(hundreds))
	    #print('The tens: {}'.format(tens))

	    return intconvert(hundreds) + ' hundred' + ' and ' + intconvert(tens) if tens else intconvert(hundreds) + ' hundred'

    elif 1000 <= num <= 9999:
	    thousands, hundreds = divmod(num, 1000)
	    #print('The thousands: {}'.format(thousands))
	    #print('The hundreds: {}'.format(hundreds))
	    return intconvert(thousands) + ' thousand' + ' and ' + intconvert(hundreds) if hundreds else intconvert(thousands) + ' thousand'
	
    else:
	    print('Sorry, the number is outside of our boundaries !')


def decconvert(dec):
    """
	This is a number-word converter, but for decimals.
	
	Parameters
	-----
	dec:str
		This is the input value
	numEngA: dict
		A dictionary of values that are only up to single digits
	frstDP: int
            The first decimal place
	scndDP: int
            The second decimal place
	
	Returns
	-----
	:str
		This checks to see if there is a valid scndp, i.e., not zero,
		and then then returns a valid decmial value in English format.
	"""
    numEngA =  {
		0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
		5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
		}
    numEngB = {
        1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'fourty',
		5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety',
        }

    frstDP = int(dec[0])
    scndDP = int(dec[1])

    return ' and ' + numEngA[frstDP] + ' ' + numEngA[scndDP] if scndDP else ' and ' + numEngB[frstDP]


def minimum_format_ensurer(values):
    """
    This is a function to ensure that there is at least 2 digits to each input.

    It adds a leading or an ending zero to each single-digit entry,
    all values will be turned to str or tuples containing str to maintain the format.

    Any item not of int or float will be skipped.

    str.zfill() is a good alternative, but not so much for decimals.

    Parameters
    -------

    values: dict
       {
        'C_Nam': C_Name, 'C_Tel': C_Telephone, 'C_Per': C_Person,
        'C_TRN': C_TRN, 'D_Inv': D_Invoice,
        'D': Description, 'Q': Quantity, 'U': Unit_Amount,
        'B': Base_Amount, 'V': VAT_Amount, 'T': Total_Amount
        }
        This is the dict of old values, some str, some int, some float.

    h: str
        This is the key of each dict entry.

    i: str/int/float
        This is the value of each entry, which does not stay standard.

    Returns
    -------
    values: dict
        This is a dict of the new values, some tuples, but all will be used as str.
    """

    for h, i in values.items():
        if type(i) is int and len(str(i)) == 1:
            #print('is int !')
            i = '0' + str(i)

        elif type(i) is float:
            #print('is float !')
            AED = str(i).split('.')[0]
            FIL = str(i).split('.')[-1]

            if len(AED) == 1:
                AED = '0' + AED

            if len(FIL) == 1:
                FIL = FIL + '0'

            i = (AED, FIL)
            #print(AED, FIL)

        else:
            #print('is undesirable !')
            continue

        values[h] = i

    return values


def get_date():
    """Get's todays date from the datetime module in the requested format."""
    return datetime.today().date().strftime('%B %d %Y')

def get_values():
    """Gets the values from the CLI."""
    

def main():
    """
    First, input and get_invoice_number().
    Then we prepare the values with calculations and minimum_num_format().
    Finally, we build with build_invoice() and end with set_invoice_number().

    Parameters
    -------
    C_Name: str

    C_Telephone: str

    C_Person: str

    C_TRN: str

    C_Asked: boolean
        This is whether or not we have to ask for the customer – prefix: C_ – variables.
        In the case of repeat invoices, for example. [Depreciation soon]

    D_invoice: int
        This is received from get_invoice_number() and it is used to update through set_invoice_number()

    Description: str
        The description of the unit

    Quantity: float
        The amount ordered of each unit

    Unit_Amount: float
        The cost of each unit

    Base_Amount: float
        The Quantity * the Unit_Amount

    VAT_Amount: float
        The Base_Amount * 0.05

    Total_Amount: float
        The Base_Amount * 1.05

    values: dict
       {
        'C_Nam': C_Name, 'C_Tel': C_Telephone, 'C_Per': C_Person,
        'C_TRN': C_TRN, 'D_Inv': D_Invoice,
        'D': Description, 'Q': Quantity, 'U': Unit_Amount,
        'B': Base_Amount, 'V': VAT_Amount, 'T': Total_Amount
        }
        These values have gone through a function and have returned differently

    Returns
    -------
    None
    """

    print('Getting invoice number...')
    
    D_Invoice = get_invoice_number()

    try:
        pprint(sys.argv)
        C_Name = str(sys.argv[1])
        C_Telephone = str(sys.argv[2])
        C_Person = str(sys.argv[3])
        C_TRN =  str(sys.argv[4])

        print("Success ! Got customer details.")
        print(sys.argv[5])
        print(type(sys.argv[5]))
        
        Description = str(sys.argv[5])
        Quantity = float(sys.argv[6])
        Unit_Amount = float(sys.argv[7])
        print(Quantity)
        print(Unit_Amount)
                       
    except:   
        C_Name = str(input('What is the CUSTOMER\'S COMPANY NAME ? ') or 'University of Wollongong in Dubai')
        C_Telephone = str(input('What is the CUSTOMER\'S TELEPHONE # ? ') or '971-56-1322345')
        C_Person = str(input('Who is the CONTACT PERSON ? ') or 'Mr Wollongong')
        C_TRN =  str(input('What is the CUSTOMER\'S TRN ? ') or '12381239018')

        print("Success ! Got customer details.")

        Description = str(input('What is the DESCRIPTION ? ') or 'Printers')
        Quantity = float(input('What is the QUANTITY ? ') or 5)
        Unit_Amount = float(input('What is the UNIT AMOUNT ? ') or 50)
    
    print('Calculating values...')
    Base_Amount = round(Unit_Amount * Quantity, 2)
    VAT_Amount = round(Base_Amount * 0.05, 2)
    Total_Amount = round(Base_Amount + VAT_Amount, 2)
    
    print('Ensuring minimum format...')
    values = minimum_format_ensurer({
    'C_Nam': C_Name, 'C_Tel': C_Telephone, 'C_Per': C_Person,
    'C_TRN': C_TRN, 'D_Inv': D_Invoice,
    'D': Description, 'Q': Quantity, 'U': Unit_Amount,
    'B': Base_Amount, 'V': VAT_Amount, 'T': Total_Amount
    })
    pprint(values)
    
    print('Converting number into words...')
    #values['W'] = ''.join(['AED: ', intconvert(values['T'][0]), decconvert(values['T'][1]), ' FILS', ' only']).upper()
    values['W'] = 'WIP'
    
    print('Acquiring dates...')
    values['Date'] = get_date()

    print('Building invoices...')
    build_invoice(values)

    print('Setting invoice number...')
    set_invoice_number(D_Invoice)

    return None


if __name__ == '__main__':
    print('Starting')
    main()
    
else:
    print('hai')
