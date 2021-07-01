<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>New</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"/>
</head>
<body>
    <div class="container w-50">
        <form:form action="/ideas/new" method="post"    modelAttribute="ideas" > 
        <br>
            <p>
                <form:label path="ideaName">Idea:</form:label>
                <form:errors path="ideaName"/>
                <form:textarea path="ideaName"/>
            </p>
            <input type="submit" value="Submit New Idea" class="btn btn-success" />
        </form:form> 
    </div>
</body>
</html>