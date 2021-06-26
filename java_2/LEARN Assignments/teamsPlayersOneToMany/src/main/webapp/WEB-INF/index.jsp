<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix = "form" uri = "http://www.springframework.org/tags/form"%>

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Teams and Players</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"/>
</head>
<body>
    <h1>Teams and Players</h1>
    <hr>
    <table class="table table-dark">
        <thead>
            <tr>
                <th scope="col">ID</th>
                <th scope="col">Name</th>
                <th scope="col">City</th>
                <th scope="col">Roster(Players)</th>
            </tr>
        </thead>
        <tbody>
        <c:forEach items = '${ allTeams }' var='team'>
            <tr>
                <td>${team.id}</td>
                <td>${team.name}</td>
                <td>${team.city}</td>
                <td>
                    <ul>
                <c:forEach items = '${ team.players }' var='p'>
                    <li>${p.firstName} ${p.lastName}</li>
                </c:forEach>
                    </ul>
                </td>
            </tr>
        </c:forEach>
        </tbody>
    </table>

    <hr>
    <h3>Create a new Team</h3>
    <form:form action="/teams/create" method="post" modelAttribute="team">
        <p>
            <form:label path="name">Name</form:label>
            <form:input path="name"/>
            <form:errors class="text text-danger" path="name"/>
        </p>
        <p>
            <form:label path="city">City</form:label>
            <form:input path="city"/>
            <form:errors class="text text-danger" path="city"/>
        </p>

        <input type="submit" value="Submit"/>

    </form:form>
    <a href="/players/new">Create Player</a>
</body>
</html>