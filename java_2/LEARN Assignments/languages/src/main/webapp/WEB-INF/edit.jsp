<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
    <h1>Edit Language:</h1>
    <div>
        <form:form class="container w-50 form-control" action="/languages/${language.id}/update" method="post" modelAttribute="language">
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