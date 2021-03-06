public class POM file {
    
}
<!-- Leave the structure for your pom.xml intact! only paste over the <dependencies> tags -->  
  
  <dependencies>
       <!--Basics (for general web dev) -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>
  		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-devtools</artifactId>
			<scope>runtime</scope>
			<optional>true</optional>
		</dependency>
  		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-tomcat</artifactId>
			<scope>provided</scope>
		</dependency>
  		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
  
       <!--For handling views (to see your .jsp pages) -->
    	<dependency>
			<groupId>org.apache.tomcat.embed</groupId>
			<artifactId>tomcat-embed-jasper</artifactId>
		</dependency>
  		<dependency>
			<groupId>javax.servlet</groupId>
			<artifactId>jstl</artifactId>
		</dependency>

       <!--MySQL -->
       <!-- We will comment this section in later when we incorporate MySQL! -->
        <!-- <dependency>
			<groupId>mysql</groupId>
			<artifactId>mysql-connector-java</artifactId>
			<scope>runtime</scope>
		</dependency>
  		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-data-jpa</artifactId>
		</dependency> --> 
  
       <!--Validations -->
  		<dependency>
		    <groupId>org.springframework.boot</groupId>
		    <artifactId>spring-boot-starter-validation</artifactId>
		</dependency>
		
       <!-- Bcrypt -->
		<dependency>
			<groupId>org.mindrot</groupId>
			<artifactId>jbcrypt</artifactId>
			<version>0.4</version>
		</dependency>
	</dependencies>