<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"/>
<title>Quotes Demo</title>
</head>
<body>
    
    <h1>Quotes!</h1>
    ${allQuotes}
    <hr>
    <div>
        <table class="table table-striped">
            <thead>
            <tr>
                <th scope="col">ID#</th>
                <th scope="col">content</th>
                <th scope="col">Quoted By</th>
                <th scope="col">Rating</th>
                <th scope="col">Users Who Like Quote</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <th scope="row">1</th>
                <td>Mark</td>
                <td>Otto</td>
                <td>@mdo</td>
                <td>@mdo</td>
            </tr>
            </tbody>
        </table>
    </div>
</body>
</html>