<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Edit Pet</title>
</head>
<body>
    <h1>Edit pet:</h1>
    <div>
        <form:form class="container w-50 form-control" action="/pets/${pet.id}/update" method="post" modelAttribute="pet">
            <p>
                <form:label path="name">Name:</form:label>
                <form:errors class="text-danger" path="name"/>
                <form:input path="name"/>
            </p>
            <p>
                <form:label path="age">Age:</form:label>
                <form:errors class="text-danger" path="age"/>
                <form:input type="number" path="age"/>
            </p>
            <p>
                <form:label path="ownerName">Owner Name:</form:label>
                <form:errors class="text-danger" path="ownerName"/>
                <form:input type="text" path="ownerName"/>
            </p>  
            <input type="submit" value="Submit"/>
        </form:form>    
    </div>
</body>
</html>