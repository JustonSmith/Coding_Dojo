<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix = "form" uri = "http://www.springframework.org/tags/form"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"/>
<title>Quotes Demo</title>
</head>
<body>
    
    <h1>Quotes!</h1>
    ${allQuotes}
    <hr>
    <div>
        <table class="table table-striped">
            <thead>
            <tr>
                <th scope="col">ID#</th>
                <th scope="col">content</th>
                <th scope="col">Quoted By</th>
                <th scope="col">Rating</th>
                <th scope="col">Users Who Like Quote</th>
            </tr>
            </thead>
            <tbody>
                <c:forEach items='${ allQuotes }' var='q'>
                    <tr>
                        <th scope="row">${q.id}</th>
                        <td><a href="/quotes/${q.id}/info">${q.content}</a></td>
                        <td>${q.quotedBy}</td>
                        <td>${q.rating}</td>
                        <td>${q.usersWhoLike}</td>
                    </tr>
                </c:forEach>
            </tbody>
        </table>
    </div>
    <hr>
    <div>
        <form:form action="/quotes/create" method="post" modelAttribute="quote">
    <p>
        <form:label path="quotedBy">Quoted By</form:label>
        <form:errors path="quotedBy"/>
        <form:input path="quotedBy"/>
    </p>
    <p>
        <form:label path="content">Content</form:label>
        <form:errors path="content"/>
        <form:textarea path="content"/>
    </p>
    <p>
        <form:label path="rating">Rating</form:label>
        <form:errors path="rating"/>
        <form:input type="number" path="rating"/>
    </p>   
    <input type="submit" value="Submit"/>
</form:form>    
    </div>
</body>
</html>