package main;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Insert your user name");
		String userName = sc.next();
		System.out.println("Insert your password");
		String password = sc.next();
		
		User user = new User();
		Course course = new Course();
		user.setCredentials(userName, password);
		if(user.login()==true) {
			System.out.println("user token: " + user.getToken());
			System.out.println("which course do you want to register");
			String courseName = sc.next();
			if(course.isAvilable(courseName)) {
				System.out.println("Thank you");
			}
		}
		else{
			System.out.println("Invaild user name or password");
		}
		

	}

}
