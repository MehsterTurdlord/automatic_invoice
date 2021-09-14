package autoInvoice;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.IOException;

/**
 * 
 * @author Mehster Eh The Turd
 * This class is the front end of my Automatic Invoice application.
 * It's purpose is to collect input and transfer it to the python script using CLI. 
 * 
 * TODO: make the imports specific.
 * TODO: Extract the CLIexperience function to its the proper function so that the exception does not matter.
 *
 */
public class GUI extends JFrame implements ActionListener {

	//components
	private Container c;
	private JLabel title;
	private JLabel c_nam;
	private JTextField c_nam_t;
	private JLabel c_tel;
	private JTextField c_tel_t;
	private JLabel c_per;
	private JTextField c_per_t;
	private JLabel c_trn;
	private JTextField c_trn_t;
	private JLabel i_des;
	private JTextField i_des_t;
	private JLabel i_qua;
	private JTextField i_qua_t;
	private JLabel i_uni;
	private JTextField i_uni_t;
	private JButton sub;
	private JButton res;
	private JLabel report;
	
	/**
	 * The main method is how this program gets run.
	 * 
	 * @param args an allowance of any String variables to enter in
	 * @throws Exception
	 */
	public static void main(String[] args) throws Exception { GUI f = new GUI(); }
	
	
	/**
	 * 	 * This is a constructor of the Form GUI
		 *  
		 * Variables necessary, viz.: Company Name: str, Telephone No: str, Contact Person: str, Customer_TRN: str, 
		 *  Description: str, QTY: int, Unit_Price: int.
		 *  
		 * The customer data should not be reset unless the 'res' button is clicked.
		 * 
		 * The invoice data should be reset every time the 'sub' button is clicked.
	 */
	public GUI () {
		setTitle("Automatic Invoice");
		setBounds(300, 90, 700, 650);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setResizable(false);
		
		c = getContentPane();
		c.setLayout(null);
		
		// STEP 1: Establish the variable
		// STEP 2: Set it to the constructor call – you can set the visible text here.
		// STEP 3: Set the Font
		// STEP 4: Set the size
		// STEP 5: Set the Location
		// STEP 6: add it to the container.
						
		title = new JLabel("Automatic Invoice");
		title.setFont(new Font("Arial", Font.PLAIN, 30));
		title.setSize(300, 30);
		title.setLocation(230, 30);
		c.add(title);
		
		c_nam = new JLabel("Customer Name");
		c_nam.setFont(new Font("Arial", Font.PLAIN, 20));
		c_nam.setSize(200, 20);
		c_nam.setLocation(100, 100);
		c.add(c_nam);
		
		c_nam_t = new JTextField();
		c_nam_t.setFont(new Font("Arial", Font.PLAIN, 15));
		c_nam_t.setSize(300, 20);
		c_nam_t.setLocation(250, 100);
		c.add(c_nam_t);
		
		c_tel = new JLabel("Telephone No.");
		c_tel.setFont(new Font("Arial", Font.PLAIN, 20));
		c_tel.setSize(200, 20);
		c_tel.setLocation(100, 150);
		c.add(c_tel);
		
		c_tel_t = new JTextField();
		c_tel_t.setFont(new Font("Arial", Font.PLAIN, 15));
		c_tel_t.setSize(300, 20);
		c_tel_t.setLocation(250, 150);
		c.add(c_tel_t);
		
		c_per = new JLabel("Contact Person");
		c_per.setFont(new Font("Arial", Font.PLAIN, 20));
		c_per.setSize(200, 20);
		c_per.setLocation(100, 200);
		c.add(c_per);
		
		c_per_t = new JTextField();
		c_per_t.setFont(new Font("Arial", Font.PLAIN, 15));
		c_per_t.setSize(300, 20);
		c_per_t.setLocation(250, 200);
		c.add(c_per_t);
		
		c_trn = new JLabel("Customer TRN");
		c_trn.setFont(new Font("Arial", Font.PLAIN, 20));
		c_trn.setSize(200, 20);
		c_trn.setLocation(100, 250);
		c.add(c_trn);
		
		c_trn_t = new JTextField();
		c_trn_t.setFont(new Font("Arial", Font.PLAIN, 15));
		c_trn_t.setSize(300, 20);
		c_trn_t.setLocation(250, 250);
		c.add(c_trn_t);
		
		i_des = new JLabel("Description");
		i_des.setFont(new Font("Arial", Font.PLAIN, 20));
		i_des.setSize(100, 20);
		i_des.setLocation(100, 300);
		c.add(i_des);
		
		i_des_t = new JTextField();
		i_des_t.setFont(new Font("Arial", Font.PLAIN, 15));
		i_des_t.setSize(300, 20);
		i_des_t.setLocation(250, 300);
		c.add(i_des_t);
		
		i_qua = new JLabel("Quantity");
		i_qua.setFont(new Font("Arial", Font.PLAIN, 20));
		i_qua.setSize(100, 20);
		i_qua.setLocation(100, 350);
		c.add(i_qua);
		
		i_qua_t = new JTextField();
		i_qua_t.setFont(new Font("Arial", Font.PLAIN, 15));
		i_qua_t.setSize(300, 20);
		i_qua_t.setLocation(250, 350);
		c.add(i_qua_t);
		
		i_uni = new JLabel("Unit Price");
		i_uni.setFont(new Font("Arial", Font.PLAIN, 20));
		i_uni.setSize(100, 20);
		i_uni.setLocation(100, 400);
		c.add(i_uni);
		
		i_uni_t = new JTextField();
		i_uni_t.setFont(new Font("Arial", Font.PLAIN, 15));
		i_uni_t.setSize(300, 20);
		i_uni_t.setLocation(250, 400);
		c.add(i_uni_t);
		
		res = new JButton("Reset Customer Data");
		res.setFont(new Font("Arial", Font.BOLD, 15));
		res.setSize(200, 30);
		res.setLocation(80, 550);
		res.addActionListener(this);
		c.add(res);
		
		sub = new JButton("Build This Invoice");
		sub.setFont(new Font("Arial", Font.BOLD, 15));
		sub.setSize(200, 30);
		sub.setLocation(400, 550);
		sub.addActionListener(this);
		c.add(sub);
		
		report = new JLabel("");
		report.setFont(new Font("Arial", Font.ITALIC, 20));
		report.setSize(500,20);
		report.setLocation(100, 480);
		c.add(report);

		setVisible(true);
	} // end of constructor

	
	/**
	 * Returns whether the string is pure integer or not.
	 * The test argument must be a trimmed string.
	 * 
	 * 
	 * @param test the trimmed down text of one of a text field
	 * @return
	 */
	public static boolean OnlyInt(String test) {
		int n = test.length();
		
		for ( int i = 0; i <n; i++ ) {	
			if (test.charAt(i) >= '0' && test.charAt(i) <='9' ) {return true;}
			else { return false; }
			
		}
		
		return false;
	}
	
	
	/**
	 * This method transfers the variables to the Python script using the command line interface.
	 * A list comes in from but we extract from the list rather than use it as is.
	 * 
	 * I could add the error stream from python to this, but...
	 * 
	 * This does not work !!!
	 * 
	 * @param an immutable list which is transfered item by item into the CLI
	 */
	public void CLIexperience() {
		ProcessBuilder builder = new ProcessBuilder("cmd.exe", "/c","cd \"C:\\Users\\peme8\\Documents\\GitHub\\Automatic_Invoice\" && dir");
		builder.redirectErrorStream();
		try {
			Process p = builder.start();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	
	/**
	 *  This method determines the results of whenever a button is pressed.
	 */
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == sub) {
				
				// Validation – presence and lookup check
				if ( !(c_trn_t.getText().trim().length() == 10)) { report.setText("TRN is 10 characters only"); }
				else if ( !(OnlyInt(i_qua_t.getText().trim())) ) { report.setText("Quantity should be in numbers and not empty !"); }
				else if ( !(OnlyInt(i_uni_t.getText().trim())) ) { report.setText("Unit Price should be in numbers and not empty !"); }
				else {			
					
					// Data clearance – except for customer data
					String empty = "";
					i_des_t.setText(empty);
					i_qua_t.setText(empty);
					i_uni_t.setText(empty);
					
					report.setText("");
					
				}
						
		} // cluster of commands for if 'Build This Invoice' is clicked
		
		else {
			
			String empty = "";
			c_nam_t.setText(empty); 
			c_tel_t.setText(empty); 
			c_per_t.setText(empty); 
			c_trn_t.setText(empty);
			i_des_t.setText(empty);
			i_qua_t.setText(empty);
			i_uni_t.setText(empty);	
			
			report.setText("Input Data Reset");
		
			
		} // cluster of commands for if 'Reset Customer Data' is clicked
	}
}
