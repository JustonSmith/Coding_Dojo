<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix = "form" uri = "http://www.springframework.org/tags/form"%>

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Dojos and Ninjas</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"/>
</head>
<body>
    <h1>Dojos and Ninjas</h1>
    <hr>
    <table class="table table-dark">
        <thead>
            <tr>
                <th scope="col">ID</th>
                <th scope="col">Location</th>
                <th scope="col">Cohort</th>
            </tr>
        </thead>
        <tbody>
        <c:forEach items = '${ allDojos }' var='dojo'>
            <tr>
                <td>${dojo.id}</td>
                <td>${dojo.name}</td>
                <td>
                    <ul>
                <c:forEach items = '${ dojo.ninjas' } var='n'>
                    <li>${n.firstName} ${n.lastName} ${n.id}</li>
                </c:forEach>
                    </ul>
                </td>
            </tr>
        </c:forEach>
        </tbody>
    </table>

    <hr>
    <h3>Create a new Dojo</h3>
    <form:form action="/dojos/create" method="post" modelAttribute="dojo">
        <p>
            <form:label path="name">Name</form:label>
            <form:input path="name"/>
            <form:errors class="text text-danger" path="name"/>
        </p>

        <input type="submit" value="Submit"/>

    </form:form>
    <a href="/dojos/new">Create Dojo</a>
</body>
</html>