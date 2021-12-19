import cherrypy
import sqlite3
import os
local_dir = os.path.dirname(__file__)
class CadPrincipal:
    @cherrypy.expose()
    def index(self):
        html = '''<head>
    <meta charset="utf-8"/>
    <title>registrar</title>
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
.reg{
    width: 280px;
    position:absolute;
    top:50%;
    left:40%;
    transform:translate(-50%,-50%);
    color:red;
}
.tt h1{font-size:60px;
    text-decoration: underline ;
}

.text{
    width:100%;
    overflow: hidden;
    font-size: 25px;
    padding: 8px 0;
    margin: 10px 0;
}

.text label{font-size:20px;
            color:black;
}
.tt{
    width: 280px;
    position:absolute;
    top:1%;
    left:38%;
    color:red;
}

.secreg{
    width: 280px;
    position:absolute;
    top:31%;
    left:50%;
    color:black;
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

.pos{
    position:absolute;
    bottom:15%;
    left:42%;
}

.voltar{
    position:absolute;
    bottom:8%;
    left:3%;
}

    </style>
</head>
<body>
    <div class="topo">&nbsp</div>
    <form action="cad_usuario" method="GET">
        <div class="tt" >
            <h1>Registrar:</h1>
        </div>
        <div class="reg">
                <div class="text">
                    <label for="user">Nome:</label><br/>
                    <input  id="user" type="text" placeholder="Nome do Usuario" name="tnome" value="" required="required" maxlength="40" autofocus="true"/>
                </div>
        
                <div class="text">
                    <label for="pw">Senha:</label><br/>
                    <input id="pw"  type="password" placeholder="Digite sua senha" name="tsenha" value="" required="required" maxlength="15"/>
                    <br/>
                    <input type="password" placeholder="Digite sua senha novamente" name="tsenha2" value="" required="required" maxlength="15" />
                </div>
                <div class="text">
                    <label for="pic">Selecione sua foto:</label><br/>
                    <input type="file" id="pic" size="40"   accept=".png, .jpg, .jpeg"/>                   
                </div>
        </div>
        <div class="secreg">
            <div class="text">
                <label for="email">E-mail:</label><br/>
                <input type="email"  size="30" placeholder="generico@genericomail.com" required="required" name="temail" value=""/>
            </div>
            <div class="text">
                <label for="fone">Telefone:</label><br/>
                <input type="text"  size="30" pattern="\(\d{2}\)\s\d{5}-\d{4}" title="(99) 99999-9999" required="required" name="ttelefone" value=""/>           
            </div>
            <div class="text">
                <label for="cep">CEP:</label><br/>
                <input type="number"  size="30"  required="required" min="0" max="999999999" step="1" name="tcep" value=""/>
            </div>
        </div>
        <div class="pos">
            <input  class="btn" type="submit"  value="Finalizar Registro"/>
        </div>
    </form>
        <div class="voltar">
            <a href="../"><button class="btn">Voltar</button></a>
        </div> 
    <div class="fim">&nbsp</div>  
</body>
         '''
        return html

    @cherrypy.expose()
    def cad_usuario(self,tnome,tsenha,tsenha2,temail,ttelefone,tcep):
        sucesso = True
        con = sqlite3.connect('BDSite.db')
        cur = con.cursor()
        if tsenha == tsenha2:
            tsobre = ' '
            tcpf = 0
            sql = "insert into Usuarios (Nome, Senha, Email, Telefone, CEP, Sobre, CPF) values ('%s', '%s', '%s', '%s', %s,'%s',%s)" %(tnome,tsenha,temail,ttelefone,tcep,tsobre,tcpf)
            try:
                cur.execute(sql)
                con.commit()
            except:
                sucesso = False
        else:
            sucesso = False
        con.close()
        if not sucesso:
            return "<h2>Erro no Cadastro!! <a href='/.'> Clique  aqui</a> para retornar</h2>"
        else:
            raise cherrypy.HTTPRedirect('/.')



server_config = {
    'server.socket_host':'127.0.0.1',
    'server.socked_port':82
}
local_config ={
    '/':{'tools.staticdir.on':True, 'tools.staticdir.dir':local_dir}
}

