<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Product Info</title>
</head>
<body>
    <h1>Here's the info for product number: ${productToShow.id} </h1>
    <p>Name: ${productToShow.name}</p>
    <p>Description: ${productToShow.description}</p>
    <p>Price: ${productToShow.price}</p>

    <h3>categories product belongs to:</h3>
    <p>${productToShow.categories}</p>

    <ul>
        <c:forEach items='${productToShow.categories}' var="c">
            <li>
                ${c.name}
            </li>
        </c:forEach>
    </ul>

    <h5>${allCategories}</h5>

    <br>
    <h3>Add product to categories</h3>
    <form action="/addCategory/${productToShow.id}" method="POST ">
        <select name="selected_category" id="">
            <c:forEach items='${ allCategories }' var="c">
                <option value="${c.id}">${c.name}</option>
            </c:forEach>
        </select>
    </form>
</body>
</html>