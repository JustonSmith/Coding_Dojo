package com.codingdojo.javaBeltExam.models;

import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.validation.constraints.Email;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.Size;

public class UserLogin {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	@NotEmpty(message="Email is required.")
	@Email(message="Please enter a valid email.")
	private String email;
	
	@NotEmpty(message="Password is required.")
	@Size(min=8, max=128, message="Password must be between 8 and 128 characters.")
	private String password;
	
	public UserLogin() {
		
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}
	
}
