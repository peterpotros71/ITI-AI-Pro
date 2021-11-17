package main;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		try {
			FileInputStream fis = new FileInputStream("C:\\Users\\hp\\eclipse-workspace\\hw03\\testread.txt");
			FileOutputStream fos = new FileOutputStream("C:\\Users\\hp\\eclipse-workspace\\hw03\\testwrite.txt");
			try {
				int ch = fis.read();
				while(ch != -1) {
					System.out.print((char)ch);
					fos.write(ch);
					ch = fis.read();
				}
				fis.close();
				fos.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			
		}
		
		
		

	}

}
