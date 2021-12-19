import cherrypy
import sqlite3
import os

from PerfilUsuario import Perfil2
from alterardadosusuario import Alterar
from cadprincipal import CadPrincipal

local_dir = os.path.dirname(__file__)


class LogPrincipal:
    @cherrypy.expose()
    def index(self):
        html = '''<head>
    <meta charset="utf-8"/>
    <title>login</title>
    <link rel="stylesheet" type="text/css" href="login-css.css"/>
    <style type="text/css">
          .topo {
        background-color: red;
        margin: 0;
        padding: 0;
            }
        .fim {
        background-color: red;
        position:absolute;
        bottom:0;
        width:100%;
            }
        body{
    margin:0;
    padding:0;
    font-family: sans-serif;
}
.login{
    width: 280px;
    position:absolute;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
    color:red;
}

.login h1{
    float:left;
    font-size:40px;
    border-bottom:6px solid;
    margin-bottom:50px;
}

.text{
    width:100%;
    overflow: hidden;
    font-size: 25px;
    padding: 8px 0;
    margin:8px 0;
    border-bottom: 1px solid red;
}

.btn{
    background-color: white;
    color: black;
    border: 3px solid #f44336;
    transition-duration: 0.4s;
    border-radius: 8px;
    padding: 10px 32px;
    text-align: center;
    font-size: 13px;
    display: inline-block;
    font-family: Verdana;
    font-weight: 500;
    width:100%;
}

.btn:hover{
    background-color: #f44336;
    color: white;
    cursor: pointer;
}

.text input{
    border:none;
    outline:none;
}
    </style>
</head>
<body>
    <div class="topo">&nbsp</div>
    <form action="login" method="GET">
        <div class="login">
            <h1>Login</h1>
            <div class="text">
                <input type="text" placeholder="Nome..." name="tnome" value="" required="required" maxlength="30" autofocus="true"/>
            </div>
    
            <div class="text">
                <input type="password" placeholder="Senha..." name="tsenha" value="" required="required" maxlength="20"/>
            </div>
            <br/>
            <a href=""><button class="btn" type="submit">Fazer Login</button></a>
    </form>
        <a href="/cad/"><p style="font-size:15px">Não tem conta? Registre-se !</p></a>
    </div>
    <div class="fim">&nbsp</div>
</body>'''
        return html

    @cherrypy.expose()
    def login(self, tnome, tsenha):
        con = sqlite3.connect('BDSite.db')
        cur = con.cursor()
        cur.execute("Select Nome,Senha from Usuarios where Nome ='" + tnome + "' and Senha ='" + tsenha + "'")
        dados = cur.fetchall()
        if len(dados) > 0:
            existe = True
        else:
            existe = False
        cur.close()
        con.close()
        if not existe:
            raise cherrypy.HTTPRedirect('/.')
        else:
            arq = open('valor.txt', 'w')
            arq.write(tnome)
            arq.close()
            raise cherrypy.HTTPRedirect('/per')

    def set_valor(self, tnome):
        self.__nome = tnome

    def get_valor(self):
        return self.__nome






server_config = {
    'server.socket_host': '127.0.0.1',
    'server.socked_port': 82
}
local_config = {
    '/': {'tools.staticdir.on': True, 'tools.staticdir.dir': local_dir}
}
cherrypy.config.update(server_config)

