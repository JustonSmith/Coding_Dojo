package com.codingdojo.javaBeltExam.models;

import java.util.Date;
import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.ManyToMany;
import javax.persistence.OneToMany;
import javax.persistence.PrePersist;
import javax.persistence.PreUpdate;
import javax.persistence.Table;
import javax.persistence.Transient;
import javax.validation.constraints.Email;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.Size;

import org.springframework.format.annotation.DateTimeFormat;

@Entity
@Table(name="users")
public class User {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	@NotEmpty(message="name required.")
	@Size(min=3, max=30, message="name must be between 3 and 30 characters.")
	private String name;
	
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
	
	@OneToMany(mappedBy = "creator", fetch = FetchType.LAZY)
	private List<Idea> ideas;
	@ManyToMany(fetch = FetchType.LAZY)
	@JoinTable(name = "users_ideas", joinColumns = @JoinColumn(name = "user_id"), inverseJoinColumns = @JoinColumn(name = "idea_id"))
	private List<Idea> likedIdeas;
	
	@Column (updatable=false)
	 @DateTimeFormat(pattern="yyyy-MM-dd")
	 private Date createdAt;
	 @DateTimeFormat(pattern="yyyy=MM-dd")
	 private Date updatedAt;
	 
	 @PrePersist
	 protected void onCreate() {
		 this.createdAt = new Date();
	 }
	 @PreUpdate
	 protected void onUpdate() {
		 this.updatedAt = new Date();
	 }
	
	
	public User() {
		
	}
	
	public User(String name, String email, String password) {
		this.name = name;
		this.email = email;
		this.password = password;
	}
	public Long getId() {
		return id;
	}
	public void setId(Long id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
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
	public List<Idea> getIdeas() {
		return ideas;
	}
	public void setIdeas(List<Idea> ideas) {
		this.ideas = ideas;
	}
	public List<Idea> getLikedIdeas() {
		return likedIdeas;
	}
	public void setLikedIdeas(List<Idea> likedIdeas) {
		this.likedIdeas = likedIdeas;
	}
	public Date getCreatedAt() {
		return createdAt;
	}
	public void setCreatedAt(Date createdAt) {
		this.createdAt = createdAt;
	}
	public Date getUpdatedAt() {
		return updatedAt;
	}
	public void setUpdatedAt(Date updatedAt) {
		this.updatedAt = updatedAt;
	}
	public boolean isPresent() {
		return false;
	}
	
	
}
