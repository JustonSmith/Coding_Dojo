<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Languages</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>
<body>
    <br>
    <h1>Favorite Languages</h1>
    <hr>
    <table class="table table-dark">
        <thead>
            <tr>
                <th scope="col">Id:</th>
                <th scope="col">Language:</th>
                <th scope="col">Creator:</th>
                <th scope="col">Version:</th>
                <th scope="col">Actions:</th>
            </tr>
        </thead>
        <tbody>
        <c:forEach items="${allPets}" var="language">
            <tr>
                <td>${language.id}</td>
                <td>${language.langName}</td>
                <td>${language.creator}</td>
                <td>${language.version}</td>
                <td><a href="/languages/${language.id}">View</a> || <a href="/languages/${language.id}/edit">Edit</a> || <a href="languages/${language.id}/delete">Delete</a></td>
            </tr>
        </c:forEach>
        </tbody>
    </table>
    <hr>
    <div>
        <h1>Create new pet:</h1>
        <form:form class="container w-50 form-control" action="/languages/create" method="post" modelAttribute="language">
            <p>
                <form:label path="langName">Language:</form:label>
                <form:errors class="text-danger" path="langName"/>
                <form:input path="langName"/>
            </p>
            <p>
                <form:label path="creator">Creator:</form:label>
                <form:errors class="text-danger" path="creator"/>
                <form:input type="number" path="creator"/>
            </p>
            <p>
                <form:label path="version">Version:</form:label>
                <form:errors class="text-danger" path="version"/>
                <form:input type="number" path="version"/>
            </p>  
            <input type="submit" value="Submit"/>
        </form:form>    
    </div>

</body>
</html>