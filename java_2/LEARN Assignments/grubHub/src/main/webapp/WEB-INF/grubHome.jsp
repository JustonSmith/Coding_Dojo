<%@taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>

<%@ page language="java" contentType="text/html; charset=UTF-8"

    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1> Welcome to grubhub bootleg</h1>
	<div>
		<p>The home of Timon and Pumba, the ultimate grubbers.</p>
		${10+100}
		
		${nameVariable}
		${numBelts}
		
		<a href="/newOrder">Order some grub, yo!</a>
		
	</div>
</body>
</html>