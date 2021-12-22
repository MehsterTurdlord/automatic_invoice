from tkinter import Tk, Button, Entry, Label, messagebox, Frame
from tkinter.constants import LEFT, RIGHT, W, E, SUNKEN
import DocumentBuilder
from pprint import pprint

top = Tk();
top.title('Invoice Writer');

# Starting variables
screen_count = 0;
visible_count = 0;
cWidgets = [];
cScreens = [];
pWidgets = [];
pScreens = [];

# functions
def _clearFew():
    """A function to clear up a few items, the product items."""
    print('Clearing product entries...')
    for item in pWidgets:
        pprint(item)
        item[1].delete(0, ( len(item[1].get()) + 1 ));
    
    return None


def _clearAll():
    """A function to clear up all items, including the customer items."""
    
    _clearFew();

    print('Clearing customer entires...');
    for item in cWidgets:
        pprint(item)
        item[1].delete(0, ( len( item[1].get() ) + 1 ));
    
    return None


def _sendForward():
    """Sends the data to Document Builder to build the Documents."""
    details = []

    if not _checkCustomer():
        messagebox.showinfo('Submission Results', 'Failed ! Missing customer data.');
        return None

    elif not _checkScreens():
        messagebox.showinfo('Submission Results', 'Failed ! Missing product data.');
        return None

    print('Collating all details')
    for item in cWidgets:
        pprint(item);
        details.append(item[1].get());

    for item in pWidgets:
        pprint(item)

        if (item[1].get()).strip() == "":
            continue # ensures no empty product entries will be sent.

        details.append(item[1].get());
    
    print('Sending details forward...')
    pprint( details );
    DocumentBuilder.main( details );

    messagebox.showinfo('Submission Results', 'Success ! Created Document');

    return None


def _checkCustomer():
    """Checks the customer entries for potential data loss.
    
    arguments
        data_present | boolean
            a check whether there is data within the customer screen.
    returns
         data_present | boolean
            a check whether there is data within the customer screen.
    """
    data_present = False;

    for item in cWidgets:
        if item[1].get().strip() != "":
            data_present = True;

    return data_present


def _checkProduct( i ):
    """Checks the product entries for potential data loss.
    
    arguments
        data_present | boolean
            a check whether there is data within a screen.
    returns
        data_present | boolean
            a check whether there is data within a screen.
    """
    data_present = False;

    for n in range(0, 3):
        if (pWidgets[ n + ( i * 3 ) ][1]).get().strip() != "":
            print("Data found !");
            data_present = True;
            break;
    
    return data_present


def _checkScreens():
    """Checks the screen for potential data loss.

    arguments
        data_present | boolean
            a check whether there is data within a screen

    returns
        data_present | boolean
            a check whether there is data within a screen
    """

    data_present = False;
    for i in range( 0, screen_count ):
        data_present = _checkProduct(i);

        if data_present:
            print('Data found !')
            break;

    return data_present


def addProduct():
    """
    Adds a new product entry.
   
    arguments
        screen_count | int
            the count of the amount of screens in use.
        
        visible_count | int
            the count of which screen is in view.

    return
        None
    """

    global screen_count, visible_count;
    i = 2;

    pScreens.append(
            Frame( top, height = 200, width = 300, borderwidth = 1, relief = SUNKEN )
        );
    
    pScreens[screen_count].grid( row = 0, column = 3, padx = 10, pady = 10, rowspan = 4, columnspan = 3 );
 
    print("Adding new product...")
      
    for item in ["Description", "Quantity", "Unit Amount"]:
        pWidgets.append((
        Label( pScreens[screen_count], text = (item + ": "), height = 1, width = 12 ),
        Entry( pScreens[screen_count], bd = 5, borderwidth = 2, )
        ));

    print("i  = {} | screen_count  = {}".format(i, screen_count))
    
    for item in pWidgets:
        item[0].grid( row = i, column = 3, padx = 2, pady = 2 );
        item[1].grid( row = i, column = 4, padx = 2, pady = 2 );
        #print("i  = {}".format(i));
        i += 1;

    pTitle = Label(pScreens[screen_count], text = ( "Product #" + str( screen_count + 1 )), height = 1, width = 10 );
    pTitle.grid(row = 1, column = 3, columnspan = 2, sticky = (E, W) );
    
    screen_count += 1;
    visible_count += 1;

    print(screen_count);
    pprint(pScreens);
    
    return None


def removeProduct( i = ( len(pScreens) - 1 ) ):
    """
    Removes a product entry.
   
    arguments
        screen_count | int
            the count of the amount of screens in use.
        
        visible_count | int
            the count of which screen is in view.

    return
        None
    """
    global screen_count, visible_count;
    
    if _checkProduct(i):
        messagebox.showinfo('ERROR', 'There is data in the last product !');
        print('Unsuccessful removal ! imp var = screen_count {} | visible_count {} | '.format(screen_count, visible_count));
        return None
    
    
    print("Removing last product...");
          
    pWidgets.pop(i);
    pScreens.pop(i);
    screen_count -= 1;
    #visible_count -= 1;
        
    previousPage();
    
    print('Successful removal ! imp var = screen_count {} | visible_count {} | '.format(screen_count, visible_count))
        
    return None


def previousPage():
    """
    Turns to the previous page.
   
    arguments
        screen_count
            the count of the amount of screens in use.
        
        visible_count
            the count of which screen is in view.

    return
        None
    """

    global screen_count, visible_count;
    
    if visible_count == 1:
        print('Outside last page limit ! imp var = screen_count {} | visible_count {} | '.format(screen_count, visible_count));
        return None
    
    visible_count -= 1;
    pScreens[ visible_count - 1 ].lift();
    print('Successful last page ! imp var = screen_count {} | visible_count {} | '.format(screen_count, visible_count));
    
    return None


def nextPage():
    """Turns to the next page.
   
    arguments
        screen_count
            the count of the amount of screens in use.
        
        visible_count
            the count of which screen is in view.

    return
        None
    """

    global screen_count, visible_count;

    if ( screen_count > visible_count ):
        visible_count += 1;
        pScreens[ visible_count - 1 ].lift();

        print('Successful next page ! imp var = screen_count {} | visible_count {} | '.format(screen_count, visible_count));
    
    else: 
        print('Outside next page limit ! imp var = screen_count {} | visible_count {} | '.format(screen_count, visible_count));
    
    return None


def cIntialiser():
    """Dynamically introduces a statically set set of items - this time from a list.

    arguments 
    cWidgets | list
        this is where all the customer metadata gets introduced into labels, entries, etc.
    
    returns
        None
    
    """
    print('Initialising the customer metadata...')

    i = 1;

    cScreens.append(
        Frame(top, height = 300, width = 300, borderwidth = 1, relief = SUNKEN )
    );

    cScreens[0].grid(row = 0, column = 0, padx = 2, pady = 2, rowspan = 5, columnspan = 2 );

    for item in ["Name", "Telephone", "Contact", "TRN"]:
        cWidgets.append((
        Label( cScreens[0], text = (item + ": "), height = 1, width = 10 ),
        Entry( cScreens[0], bd = 5, borderwidth = 2 )
        ));
    
    for item in cWidgets:
        item[0].grid( row = i, column = 0, padx = 1, pady = 1 );
        item[1].grid( row = i, column = 1, padx = 1, pady = 1 );
        i += 1;
    
    cTitle = Label( cScreens[0], text = ("Customer Details"), height = 1, width = 20 );
    cTitle.grid( row = 0, column = 0, padx = 2, pady = 4, columnspan = 2 );

    return None


def bIntialiser():
    """Intialises the buttons."""
    
    cbuttonsFrame = Frame(top, height = 200, width = 300, borderwidth = 1, relief = SUNKEN );
    pbuttonsFrame = Frame(top, height = 200, width = 300, borderwidth = 1, relief = SUNKEN );

    cbuttonsFrame.grid( row = 5, column = 0, padx = 1, pady = 1, rowspan = 2, columnspan = 3 );
    pbuttonsFrame.grid( row = 5, column = 3, padx = 1, pady = 1, rowspan = 2, columnspan = 3 );

    clrFew = Button(cbuttonsFrame, text = 'Same Customer', command = _clearFew, height = 1, width = 10      );
    clrAll = Button(cbuttonsFrame, text = 'Next Customer', command = _clearAll, height = 1, width = 10      );
    submit = Button(cbuttonsFrame, text = 'Submit Invoice', command = _sendForward, height = 4, width = 10  );
    newPrd = Button(pbuttonsFrame, text = 'Add Product', command = addProduct, height = 1, width = 10       );
    remPrd = Button(pbuttonsFrame, text = 'Remove Product', command = removeProduct, height = 1, width = 10 );
    nxPage = Button(pbuttonsFrame, text = '>', command = nextPage, height = 1, width = 2                    );
    prPage = Button(pbuttonsFrame, text = '<', command = previousPage, height = 1, width = 2                    );

    #pgCont = Label(pbuttonsFrame, text = ('Product screen_count of ' + str(screen_count)), height = 1, width = 15 );

    clrFew.grid( row = 5, column = 0, padx = 2, pady = 2 );
    clrAll.grid( row = 6, column = 0, padx = 2, pady = 2 );
    submit.grid( row = 5, column = 1, padx = 2, pady = 2, rowspan = 2 );
    prPage.grid( row = 5, column = 2, padx = 2, pady = 2 );
    #pgCont.grid( row = 5, column = 3, padx = 2, pady = 2 );
    nxPage.grid( row = 5, column = 4, padx = 2, pady = 2 );
    newPrd.grid( row = 6, column = 2, padx = 2, pady = 2 );
    remPrd.grid( row = 6, column = 4, padx = 2, pady = 2 );

    return None


def pIntialiser():
    """Intialises the product."""
    addProduct();
    return None


# Starting functions
cIntialiser();
pIntialiser();
bIntialiser();

top.mainloop();
