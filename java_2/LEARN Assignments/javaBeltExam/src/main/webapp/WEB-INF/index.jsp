<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix = "form" uri = "http://www.springframework.org/tags/form"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"/>
<title>Ideas</title>
</head>
<body>
    
    <h1>Welcome, ${newUser.name} </h1>
    <button class="btn btn-block"><a href="/logout">Logout</a></button>
    <button class="btn btn-block"><a href="/ideas/new">New Idea</a></button>
    <div>
        <table class="table table-striped">
            <thead>
            <tr>
                <th scope="col">Idea</th>
                <th scope="col">Created By</th>
                <th scope="col">Content</th>
                <th scope="col">Likes</th>
                <th scope="col">Like/Unlike</th>
                <th scope="col">Edit</th>
                <th scope="col">Delete</th>
            </tr>
            </thead>
            <tbody>
                <c:forEach items='${ ideas }' var='ideas'>
                    <tr>
                        <th scope="row">${ideas.id}</th>
                        <td>${ideas.creator.name}</td>
                        <td><a href="/show/${ideas.id}">${ideas.ideaName}</a></td>
                        <td>${ideas.likers.size()}</td>
                        <td><a href="/like/${ideas.id}">Like</a> || <a href="/unlike/${ideas.id}">Unlike</a></td>
                        <td><a href="/ideas/edit/${ideas.id}">Edit</a></td>
                        <td><a href="/ideas/delete/${ideas.id}">Delete</a></td>
                    </tr>
                </c:forEach>
            </tbody>
        </table>
    </div>
</body>
</html>
<!-- <body>
    <div class="container col-sm-8" style="margin-top:30px">
        <h1>Welcome,
            "${newUser.name}"
        </h1>
        <button class="btn btn-block"><a href="/logout">Logout</a></button>
        <div class="row">
            <div class="col-sm-6">
                <h2>Ideas</h2>
            </div>
            <div class="container">
                <table>
                    <thead>
                        <tr>
                            <th>Idea </th>
                            <th>Created by</th>
                            <th>Likes</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <c:forEach items="${ideas}" var="ideas">
                            <tr>
                                <td><a href="/show/${ideas.id}">${ideas.ideaName }</a></td>
                                <td>${ideas.creator.name}</td>
                                <td>${ideas.likers.size() }</td>
                                <c:if test="${ideas.creator.id != user.id }">
                                    <c:if test="${ideas.likers.contains(newUser) == false }">
                                        <td>
                                            <a href="/like/${ideas.id }">Like</a>
                                        </td>
                                    </c:if>
                                    <c:if test="${ideas.likers.contains(newUser) == true }" >
                                        <td>
                                            <a href="/unlike/${ideas.id }">Unlike</a>
                                        </td>
                                    </c:if>
                                </c:if>
                            </tr>
                        </c:forEach>
                    </tbody>
                </table>
                <button class="btn btn-block"><a href="/ideas/new">New Idea</a></button>
            </div>
        </div>
    </div>
</body> -->
</html>