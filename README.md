# testeigs by Sérgio Leão
<p> 
To up system in dev mod: <br>
    <pre>
    git clone https://github.com/sergioleao/testeigs.git <br>
    cd testeigs  <br>
    docker build -t igs .  <br>
    docker run -p 8000:8000 igs</p>
    </pre>
    
Login:
 <pre>
    user: igs <br>
    pass: 123456</pre>

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
    http://127.0.0.1:8000/api/v1/public/ (rest seach public for web) <br>
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
    



