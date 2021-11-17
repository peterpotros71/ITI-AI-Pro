package main;

public class User {
	
	public String dislayName;
	private String userName;
	private String password;
	public String emailAddress;
	private String token="";
	
	public void printUserInfo() {
		System.out.print("the name for the student is " + dislayName + " and the email is " + emailAddress);
	}
	
	public void setCredentials(String userName, String password) {
		this.userName= userName;
		this.password = password;
	}
	
	public boolean login() {
		if(this.userName.equals("admin")&& this.password.equals("admin")) {
			this.token = "granted";
			return true;
		}
		return false;
		
	}
	
	public String getToken() {
		return this.token;
	}

}
