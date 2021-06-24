<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Order Form</title>
</head>
<body onload="warnAboutCurry()">
    <h1>Order some BangKok Garden Special Thai Curry today, ${dateInfo}.</h1>
    <form action="/submitOrder" method="POST">
        <div class="form-group">
            <label for="">Your name</label>
            <input type="text" name="nombre" id="">
        </div>
        <div>
            <label for="">Select spice level.</label>
            <select name="spiceLevel" id="">
                <option value="">1 (mild)</option>
                <option value="">2</option>
                <option value="">3 (medium)</option>
                <option value="">4</option>
                <option value="">5 (extra spicy)</option>
            </select>
        </div>
        <div>
            <label for="">Credit Card Number</label>
            <input type="text" name="ccNum" id="">
        </div>
        <input type="submit" value="Order this Curry!">
    </form>
    <script src="/js/grubstuff.js"></script>
</body>
</html>