/*
 * Solution for day 1 of the Advent of Code 2022.
 * 
 * Hayden Walker (www.haywalk.ca), 2022-12-01
 *
 */

import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class CalorieCountingPartTwo
{
	public static void main(String[] args) throws FileNotFoundException
	{
		// Declare variables
		File inputFile; // Input file
		Scanner sc; // Scanner object to read file
		String thisLine; // Current input line
		int running; // The total for one elf
		int[] max; // Top three values

		// Initialize variables
		inputFile = new File(args[0]);
		sc = new Scanner(inputFile);
		max = new int[3];
		running = 0;	
	
		// Read until EOF
		while(sc.hasNextLine()) {
			// Get the next line
			thisLine = sc.nextLine();

			// If the line isn't blank, get the number and add it
			// to the total
			if(!thisLine.equals(""))
				running += Integer.parseInt(thisLine);

			// If the line is blank, see if this elf's total is in the
			// top three
			else {
				// Go through the top 3 array and find a place to insert
				for(int i = 2; i > -1; i--) {
					// A place to insert has been found
					if(running > max[i]) {
						// Shift all previous entries back
						for(int j = 0; j < i; j++)
							max[j] = max[j + 1];

						// Insert the new entry and stop
						max[i] = running;
						break;
					}
				}
			
				// Reset the total
				running = 0;
			}
		}

		// Close scanner and display result
		sc.close();
		System.out.println(max[0] + max[1] + max[2]);
	}
}
