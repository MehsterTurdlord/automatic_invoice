from tkinter import Tk, Button, Entry, Label, messagebox
from tkinter.constants import LEFT, RIGHT
import DocumentBuilder
from pprint import pprint

top = Tk();

# Entries
cNamLabel = Label(top, text='Name: '        );
cTelLabel = Label(top, text='Telephone: '   );
cPerLabel = Label(top, text='Contact: '     );
cTRNLabel = Label(top, text='TRN: '         );
pDesLabel = Label(top, text='Description: ' );
pQuaLabel = Label(top, text='Quantity: '    );
pCosLabel = Label(top, text='Unit Amout: '  );

cNamEntry = Entry(top, bd=5, borderwidth=2, );
cTelEntry = Entry(top, bd=5, borderwidth=2, );
cPerEntry = Entry(top, bd=5, borderwidth=2, );
cTRNEntry = Entry(top, bd=5, borderwidth=2, );
pDesEntry = Entry(top, bd=5, borderwidth=2, );
pQuaEntry = Entry(top, bd=5, borderwidth=2, );
pCosEntry = Entry(top, bd=5, borderwidth=2, );

cNamLabel.grid( row = 1, column = 0, padx=1, pady=2 );
cTelLabel.grid( row = 2, column = 0, padx=1, pady=2 );
cPerLabel.grid( row = 3, column = 0, padx=1, pady=2 );
cTRNLabel.grid( row = 4, column = 0, padx=1, pady=2 );
pDesLabel.grid( row = 5, column = 0, padx=1, pady=2 );
pQuaLabel.grid( row = 6, column = 0, padx=1, pady=2 );
pCosLabel.grid( row = 7, column = 0, padx=1, pady=2 );

cNamEntry.grid( row = 1, column = 1, padx=1, pady=2 );
cTelEntry.grid( row = 2, column = 1, padx=1, pady=2 );
cPerEntry.grid( row = 3, column = 1, padx=1, pady=2 );
cTRNEntry.grid( row = 4, column = 1, padx=1, pady=2 );
pDesEntry.grid( row = 5, column = 1, padx=1, pady=2 );
pQuaEntry.grid( row = 6, column = 1, padx=1, pady=2 );
pCosEntry.grid( row = 7, column = 1, padx=1, pady=2 );

# buttons and commands
def _clearFew():
    """A function to clear up a few items, the price items."""
    print('Clearing few entries...')
    details = [    
        pDesEntry, pQuaEntry, pCosEntry
              ]
    for item in details:
        item.delete(0, ( len(item.get()) + 1 ));
    
    return None


def _clearAll():
    """A function to clear up all items, including the customer items."""
    print('Clearing all entries...')
    details = [    
        cNamEntry, cTelEntry, cPerEntry, cTRNEntry, 
        pDesEntry, pQuaEntry, pCosEntry
              ]
    for item in details:
        item.delete(0, ( len(item.get()) + 1 ));
    
    return None


def _sendForward():
    """Sends the data to Document Builder to build the Documents."""
    print('Sending details forward...')
    details = [    
        cNamEntry.get(), cTelEntry.get(), cPerEntry.get(), cTRNEntry.get(), 
        pDesEntry.get(), pQuaEntry.get(), pCosEntry.get()
              ]

    pprint( details );
    DocumentBuilder.main( details );

    messagebox.showinfo('Submission Results', 'Success ! Created Document');

    return None


def addProduct():
    """Adds three new fields - for a new product - and changes the location of the new product button."""
    return None


clrFew = Button(top, text ='Same Customer',    command = _clearFew    );
clrAll = Button(top, text ='Clear Completely', command = _clearAll    );
submit = Button(top, text ='Submit Invoice',   command = _sendForward );

clrFew.grid( row = 8,  column = 0, padx = 1, pady = 2 );
clrAll.grid( row = 9,  column = 0, padx = 1, pady = 2 );
submit.grid( row = 10, column = 0, padx = 1, pady = 2 );

top.mainloop();
