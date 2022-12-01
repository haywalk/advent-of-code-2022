/*
 * Solution for day 1 of the Advent of Code 2022.
 * 
 * Hayden Walker (www.haywalk.ca), 2022-12-01
 *
 */

import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class CalorieCounting
{
	public static void main(String[] args) throws FileNotFoundException
	{
		// Declare variables
		File inputFile; // Input file
		Scanner sc; // Scanner object to read file
		String thisLine; // Current input line
		int running, max; // Running total for one elf, and maximum value so far

		// Initialize variables
		inputFile = new File(args[0]);
		sc = new Scanner(inputFile);
		max = 0;
		running = 0;	
	
		// Read until EOF
		while(sc.hasNextLine()) {
			// Get the next line
			thisLine = sc.nextLine();

			// If the line isn't blank, get its number
			if(!thisLine.equals("")) 
				running += Integer.parseInt(thisLine);

			// If the line is blank, check if the total since
			// the last blank line is more than the maximum so far
			else {
				if(running > max)
					max = running;
				
				running = 0;
			}
		}

		// Close the scanner and display the result
		sc.close();
		System.out.println(max);
	}
}
