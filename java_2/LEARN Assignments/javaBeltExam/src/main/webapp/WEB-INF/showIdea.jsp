<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Idea Info</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"/>
</head>
<body>
    <div>
        <h1>Idea Info: ${ideas.id}</h1>
        <p>Created by: ${ideas.creator.name}</p>
        <p>Content: ${ideas.ideaName}</p>
        <p>Likes: ${ideas.likers.size()}</p>

        <h3>Users who like this quote: {ideas.likers.id}</h3>

        <ul>
            <c:forEach items='${ideas.likers.id}' var='ideas'>
                <li>
                ${newUser.name}
                </li>
            </c:forEach>
        </ul>
        <br>
        <h3>People who like this idea:</h3>
        <form action='${ideas.id}'' method="POST">
            <select name="creator" id="">
                <c:forEach items='${ ideas.likers.id }' var= 'ideas'>
                    <option value="${u.id}">${newUser.name}</option>
                </c:forEach>
            </select>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>