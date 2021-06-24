<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Current visit count</title>
</head>
<body>
<h4>You have visited <a href="/your_server">http://your_server</a> <c:out value="${count}"/> times.</h4>
<h4><a href="/your_server">Test another visit?</a></h4>
</body>
</html>