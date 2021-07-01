<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Dashboard</title>
</head>
<body>
    <h1>Welcome, ${ loggedInUser.userName }</h1>
    <a href="/logout">Logout</a>

    <table class="table">
        <thead>
            <tr>
                <th scope="col">ID#</th>
                <th scope="col">Menu Item</th>
                <th scope="col">Uploaded By</th>
                <th scope="col">Actions</th>
            </tr>
        </thead>
        <tbody>
            <c:forEach items='${ allMenuItems }' var='m'>
                <tr>
                    <th scope="row">${m.id}</th>
                    <td><a href="/menu/${m.id}/info">${m.name}</a></td>
                    <td>${m.uploader.userName}</td>
                    <td><a href="/menu/${m.id}/edit">Edit</a> || <a href="/menu/${m.id}/delete">Delete</a></td>
                </tr>
            </c:forEach>
        </tbody>
    </table>
    <a href="/menu/new">Add new Menu Item</a>
</body>
</html>
