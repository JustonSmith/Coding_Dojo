<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="form" uri="http://www.springframework.org/tags/form"%>

<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Hello World Test</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"/>
</head>
<body>
    <h1>Pet Shelter</h1>
    <hr>
    <h1 class="">Here are the pets:</h1>
    <table class="table table-dark container w-50">
        <thead>
            <tr>
                <th scope="col">Id</th>
                <th scope="col">Name:</th>
                <th scope="col">Age:</th>
                <th scope="col">Owner:</th>
                <th scope="col">Actions:</th>
            </tr>
        </thead>
        <tbody>
        <c:forEach items="${allPets}" var="pet">
            <tr>
                <td>${pet.id}</td>
                <td>${pet.name}</td>
                <td>${pet.age}</td>
                <td>${pet.ownerName}</td>
                <td><a href="/pets/${pet.id}">View</a> || <a href="/pets/${pet.id}/edit">Edit</a> || <a href="/pets/${pet.id}/delete">Delete</a></td>
            </tr>
        </c:forEach>
        </tbody>
    </table>
    <hr>
    <div>
        <h1>Create new pet:</h1>
        <form:form class="container w-50 form-control" action="/pets/create" method="post" modelAttribute="pet">
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