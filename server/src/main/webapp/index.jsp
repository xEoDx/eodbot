<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!doctype html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="utf-8">
    <title>Welcome to EodBot!</title>
    <link rel="stylesheet" href="<c:url value='/static/node_modules/bootstrap/dist/css/bootstrap.css'/>">
    <link rel="stylesheet" href="<c:url value='/static/node_modules/font-awesome-4.5.0/css/font-awesome.min.css'/>">
    <link rel="stylesheet" href="<c:url value='/static/node_modules/ng-table/dist/ng-table.min.css'/>">
    <link rel="stylesheet" href="<c:url value='/static/css/app.css'/>">
    <script src="<c:url value='/static/node_modules/jquery/dist/jquery.min.js' />"></script>

    <!-- Angular -->
    <script src="<c:url value='/static/node_modules/angular/angular.min.js' />"></script>
    <script src="<c:url value='/static/node_modules/angular-animate/angular-animate.min.js' />"></script>
    <script src="<c:url value='/static/node_modules/angular-route/angular-route.min.js' />"></script>
    <script src="<c:url value='/static/node_modules/ng-table/dist/ng-table.min.js' />"></script>


    <!-- Bootstrap -->
    <script src="<c:url value='/static/node_modules/angular-ui-bootstrap/dist/ui-bootstrap.js' />"></script>
    <script src="<c:url value='/static/node_modules/angular-ui-bootstrap/dist/ui-bootstrap-tpls.js' />"></script>
    <script src="<c:url value='/static/node_modules/bootstrap/js/dropdown.js' />"></script>

    <!-- Eodbot -->
    <script src="<c:url value='/static/admin/routing.js' />"></script>
    <script src="<c:url value='/static/admin/app.js' />"></script>
    <script src="<c:url value='/static/admin/messages/service.js' />"></script>
    <script src="<c:url value='/static/admin/messages/controller.js' />"></script>
</head>
<body ng-app="hipChatMessagesModule">
<div ng-view class="container">

</div>
</body>
</html>