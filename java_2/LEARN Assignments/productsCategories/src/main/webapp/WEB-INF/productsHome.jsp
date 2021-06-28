<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix = "form" uri = "http://www.springframework.org/tags/form"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"/>
<title>Products and Categories</title>
</head>
<body>
    <h1>Products and Categories</h1>
    ${allProducts}
    <hr>
    <div>
        <table class="table table-striped">
            <thead>
            <tr>
                <th scope="col">ID#</th>
                <th scope="col">Name</th>
                <th scope="col">Description</th>
                <th scope="col">Price</th>
            </tr>
            </thead>
            <tbody>
                <c:forEach items='${ allProducts }' var='p'>
                    <tr>
                        <th scope="row">${p.id}</th>
                        <td><a href="/products/${p.id}/info">${p.name}</a></td>
                        <td>${p.description}</td>
                        <td>${p.price}</td>
                    </tr>
                </c:forEach>
            </tbody>
        </table>
    </div>
    <div>
        <form:form action="/products/create" method="post"   modelAttribute="product">
        <p>
            <form:label path="name">Name</form:label>
            <form:errors path="name"/>
            <form:input path="name"/>
        </p>
        <p>
            <form:label path="description">Description</form:label>
            <form:errors path="description"/>
            <form:textarea path="description"/>
        </p>
        <p>
            <form:label path="price">Price</form:label>
            <form:errors path="price"/>
            <form:input type="number" path="price"/>
        </p>   
    <input type="submit" value="Submit"/>
</form:form>    
    </div>
</body>
</html>