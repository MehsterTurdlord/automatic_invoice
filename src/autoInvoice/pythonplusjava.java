package autoInvoice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class pythonplusjava {
	public static void main(String args[]) {
		String s = null;
		
		try {
			Process p = Runtime.getRuntime().exec("python DocumentBuilder.py Bing 123 Bong 1231 Chess_Borger 20 40");
            
            BufferedReader stdInput = new BufferedReader(new 
                 InputStreamReader(p.getInputStream()));

            BufferedReader stdError = new BufferedReader(new 
                 InputStreamReader(p.getErrorStream()));

            // read the output from the command
            System.out.println("Here is the standard output of the command:\n");
            while ((s = stdInput.readLine()) != null) {
                System.out.println(s);
            }
            
            // read any errors from the attempted command
            System.out.println("Here is the standard error of the command (if any):\n");
            while ((s = stdError.readLine()) != null) {
                System.out.println(s);
            }
            
            System.exit(0);
        }
        catch (IOException e) {
            System.out.println("exception happened - here's what I know: ");
            e.printStackTrace();
            System.exit(-1);
        }
    }
}