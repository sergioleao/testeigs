# testeigs by Sérgio Leão

To up system in dev mod:
    git clone https://github.com/sergioleao/testeigs.git
    cd testeigs 
    docker build -t igs . 
    docker run -p 8000:8000 igs



user: igs
pass: 123456

public rest endpoints:
    http://127.0.0.1/api/v1/public/
private rest endpoints:
    http://127.0.0.1:8000/admin/
    http://127.0.0.1/api/v1/admin/

website public:
    http://127.0.0.1:8000/
    http://127.0.0.1:8000/listemploye/
    http://127.0.0.1:8000/api/v1/public/ (rest seach public for web)
website private:
    http://127.0.0.1:8000/admin/
    http://127.0.0.1:8000/api/v1/admin/
    http://127.0.0.1:8000/api/v1/admin/employee/ (only authenticated)
    http://127.0.0.1:8000/api/v1/admin/department/ (only authenticated)
    http://127.0.0.1:8000/api/v1/doc/ (Api documentation Swagger)
    http://127.0.0.1:8000/api/v1/redoc/ (Api documentation RedDoc)
    



