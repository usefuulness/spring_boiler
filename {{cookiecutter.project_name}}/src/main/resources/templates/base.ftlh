<!DOCTYPE html>
<html lang="de">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{cookiecutter.project_name}}</title>
    <link rel="stylesheet" type="text/css" href="/static/css/main.css">
</head>

<body>

    <header>
        <div class="header">
            <h1>{{cookiecutter.project_name}}</h1>
        </div>
    </header>

    <main>
        <#include "${contentTemplate}.ftlh">
    </main>

    <script type="text/javascript" src="/static/js/out/main.js"></script>

</body>

</html>