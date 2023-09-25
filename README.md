# testeigs by Sérgio Leão
<p> 
To up system in dev mod: <br>
    <pre>
    git clone https://github.com/sergioleao/testeigs.git <br>
    cd testeigs  <br>
    docker build -t igs .  <br>
    docker run -p 8000:8000 igs</p>
    </pre>
    
<p> 
To up without docker: <br>
    <pre>
    git clone https://github.com/sergioleao/testeigs.git <br>
    cd testeigs  <br>
    python3 -m venv venv
        on Windows:
            - .\venv\Scripts\activate.bat
        on Systens unix:
            -  source venv/bin/activate
    pip install -r requirements.txt   <br>
        on Windows:
            - py manage.py runserver
        on Linux
            python3 manage.py runserver
    </p>
    </pre>


Web Login:
 <pre>
    user: igs <br>
    pass: 123456</pre>
<pre>
Rest get Token (GET method):
    send body with insomnia or postman
    key: username  Value: igs 
    key: password  Value: 123456 
    the return will be the token that can be sent in the Header to access private endpoints through REST requests
    the token must be passed in the header as:
       key: Authorization
       Value: Token {the token obtained in the authorization endpoint request (api-token-auth)}

</pre>
<pre>
Unit Test on:
    -tests
        --test_viewset.py
</pre>

public rest endpoints:<br>
<pre>
    http://127.0.0.1/api/v1/public/ <br>
</pre>
private rest endpoints: <br>
<pre>
    http://127.0.0.1:8000/admin/ <br>
    http://127.0.0.1/api/v1/admin/ <br>
</pre>
website public: <br> 
<pre>
    http://127.0.0.1:8000/ <br>
    http://127.0.0.1:8000/listemploye/ <br>
    http://127.0.0.1:8000/api/v1/public/  <br>
</pre>
website private: <br>
<pre>
    http://127.0.0.1:8000/admin/ <br>
    http://127.0.0.1:8000/api/v1/admin/ <br>
    http://127.0.0.1:8000/api/v1/admin/employee/ (only authenticated) <br>
    http://127.0.0.1:8000/api/v1/admin/department/ (only authenticated) <br>
    http://127.0.0.1:8000/api/v1/doc/ (Api documentation Swagger) <br>
    http://127.0.0.1:8000/api/v1/redoc/ (Api documentation RedDoc) <br>
</pre>
    



