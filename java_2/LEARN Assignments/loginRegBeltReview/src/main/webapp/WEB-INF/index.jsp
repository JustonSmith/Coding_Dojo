<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Login Registration Belt Review</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>
<body class="container w-50">
    <br>
    <hr>
    <hr>
    <br>
    <div class="container w-50 border border-dark border border rounded">
        <!-- REGISTRATION -->
        <h1 class="">Register Account:</h1>
        <form:form action="/register" method="post" modelAttribute="newUser" >
            <div class="form-group">
                <label>User Name:</label>
                <form:input path="userName" class="form-control" />
                <form:errors path="userName" class="text-danger" />
            </div>
            <div class="form-group">
                <label>Email:</label>
                <form:input path="email" class="form-control" />
                <form:errors path="email" class="text-danger" />
            </div>
            <div class="form-group">
                <label>Password:</label>
                <form:password path="password" class="form-control" />
                <form:errors path="password" class="text-danger" />
            </div>
            <div class="form-group">
                <label>Confirm Password:</label>
                <form:password path="confirm" class="form-control" />
                <form:errors path="confirm" class="text-danger" />
            </div>
            <br>
            <input type="submit" value="Register" class="btn btn-primary" />
            <br>
        </form:form>
    </div>
    <br>
    <hr>
    <hr>
    <br>
    <!-- LOGIN -->
    <div class="container w-50 border border-dark border border rounded">
        <h1>Login:</h1>
        <form:form action="/login" method="post" modelAttribute="newLogin">
            <div class="form-group">
                <label>Email:</label>
                <form:input path="email" class="form-control" />
                <form:errors path="email" class="text-danger" />
            </div>
            <div class="form-group">
                <label>Password:</label>
                <form:password path="password" class="form-control" />
                <form:errors path="password" class="text-danger" />
            </div>
            <br>
            <input type="submit" value="Login" class="btn btn-success" />
        </form:form>
    </div>
    <br>
    <hr>
    <hr>
    <br>
</body>
</html>