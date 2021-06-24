package com.codingdojo.laguages.models;

import java.util.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.PrePersist;
import javax.persistence.PreUpdate;
import javax.persistence.Table;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

import org.springframework.format.annotation.DateTimeFormat;

@Entity
@Table (name="languages")
public class Language {

		@Id
		@GeneratedValue( strategy = GenerationType.IDENTITY)
		private Long id;
		
		@NotNull
		@Size(min=2, max=20, message= "language name cannot be less than 2 or more than 20 characters long.")
		private String langName;
		
		@NotNull
		@Size(min=2, max=20, message= "language name cannot be less than 2 or more than 20 characters long.")
		private String creator;
		
		@NotNull
		@Min (value= 0, message= "version number cannot be less than 0")
		private Integer version;
		
		@Column (updatable=false)
		@DateTimeFormat(pattern="yyyy-MM-dd")
		private Date createdAt;
		@DateTimeFormat(pattern="yyyy-MM-dd")
		private Date updatedAt;
		
		
		public Language() {
			
		}


		public Language(String langName, String creator, Integer version) {
			this.langName = langName;
			this.creator = creator;
			this.version = version;
		}
		
		@PrePersist
		protected void onCreate() {
			this.createdAt = new Date();
		}
		@PreUpdate
		protected void onUpdate() {
			this.updatedAt = new Date();
		}


		public Long getId() {
			return id;
		}


		public void setId(Long id) {
			this.id = id;
		}


		public String getLangName() {
			return langName;
		}


		public void setLangName(String langName) {
			this.langName = langName;
		}


		public String getCreator() {
			return creator;
		}


		public void setCreator(String creator) {
			this.creator = creator;
		}


		public Integer getVersion() {
			return version;
		}


		public void setVersion(Integer version) {
			this.version = version;
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
		
		
		
		
		
	
	
	
	
	
}
