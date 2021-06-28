<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Quote Info</title>
</head>
<body>
    <h1>Here's the info for quote number ${quoteToShow.id}</h1>
    <p>Quoted by: ${quoteToShow.quotedBy}</p>
    <p>Content: ${quoteToShow.content}</p>
    <p>Rating: ${quoteToShow.rating}</p>

    <h3>Users who like this quote:</h3>

    <ul>
        <c:forEach items='${quoteToShow.usersWhoLike}' var='u'>
            <li>
            ${u.name}
            </li>
        </c:forEach>
    </ul>

    <h5>${allUsers}</h5>
    <br>
    <h3>Add a User as one of the favoriters of this quote</h3>
    <form action="/addUserToQuote/${quoteToShow.id}" method="POST">
        <select name="selected_user" id="">
            <c:forEach items='${ allUsers }' var= 'u'>
                <option value="${u.id}">${u.name}</option>
            </c:forEach>
        </select>
        <input type="submit" value="Submit">
    </form>
</body>
</html>