package com.codingdojo.javaBeltExam.models;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.persistence.Transient;
import javax.validation.constraints.Email;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.Size;

@Entity
@Table(name="users")
public class User {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	
	@NotEmpty(message="User name is required.")
	@Size(message="please enter a valid email.")
	private String userName;
	
	@NotEmpty(message="First name is required.")
	@Size (min=3, max=30, message="Username must be between 3 and 30 characters.")
	private String firstName;
	
	@NotEmpty(message="Last name is required.")
	@Size (min=3, max=30, message="Username must be between 3 and 30 characters.")
	private String lastName;
	
	@NotEmpty(message="Email is required.")
	@Email(message="please enter a valid email.")
	private String email;
	
	@NotEmpty(message="Password is required.")
	@Size(message="please enter a valid password.")
	private String password;
	
	@Transient
	@NotEmpty(message="Confirm password is required.")
	@Size(min=8, max=128, message="Confirm password must be between 8 and 128 characters")
	private String confirm;
	
	
	public User() {
		
	}
	
	public User(String userName, String firstName, String lastName, String email, String password) {
		this.userName = userName;
		this.firstName = firstName;
		this.lastName = lastName;
		this.email = email;
		this.password = password;
	}

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getUserName() {
		return userName;
	}

	public void setUserName(String userName) {
		this.userName = userName;
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
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

	public String getConfirm() {
		return confirm;
	}

	public void setConfirm(String confirm) {
		this.confirm = confirm;
	}
	
	
	
	
	
	
	
	
}
