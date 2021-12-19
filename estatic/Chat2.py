import cherrypy
from PagProduto import *
import os
import sqlite3


class chat2:
    @cherrypy.expose
    def index(self):
        html = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="utf-8"/>
	<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
	<link rel="stylesheet" type="text/css" href="cssPerfil.css"/>
	<link rel="stylesheet" type="text/css" href="..\css.css"/>
	<title>Perfil</title>	
    <style type="text/css" media="screen">
    * {
			box-sizing: border-box; 
		}
		body {
		  display: flex;
		  min-height: 100vh;
		  flex-direction: column;
		  margin: 0;
		}
		#main {
		  display: flex;
		  flex: 1;
		}
		#main > article {
		  flex: 1;
		}
		#main > nav, 
		#main > aside {
		  flex: 0 0 20vw;
		  background: white;
		}
		
		header, footer {
		  background: white;
		  height: 20vh;
		}
		header, footer, article, nav, aside {
		  padding: 1em;
		}

.imguser{
    max-width: 10px;
    
}

.edproduto{
    height: 320px;
    position: absolute;
    width: 270px;
    border-radius: 10px;
    transition: 0.2s;
    text-align: center;
}

.textdest1{
    position: absolute;
    top: 19%;
    left: 34%;
    text-shadow: 2px 2px #EEEEEE;

}
.textdestChat{
    position: absolute;
    top: 19%;
    left: 46%;
    text-shadow: 2px 2px #EEEEEE;

}
.textLabel{
    border: 3px solid #f44336;
    font-family: Arial;
    border-radius: 10px;
    padding: 30px;
    margin-top: 25px;
    width: 47%;
    left: 27%;
    position: relative;
}

.caixaChat{

    border: 3px solid #f44336;
    font-family: Arial;
    border-radius: 10px;
    padding: 30px;
    margin-top: 25px;
    width: 47%;
    height: 90%;
    left: 27%;
    position: relative;
    margin-bottom: 25px;
}

.user-img{
    width: 7%;
    margin-top: 5px;
    margin-left: 8px;
}


.textName{
    position: absolute;
    left: 12%;
    font-size: 19px;
    top: 1%;
}

.mensagem{
    margin: 3px;
    position: relative;
    transition: 0.8s;
}

.mensagem:hover{
    box-shadow: 10px 10px 20px darkgray;
    width: 560px;
    cursor: pointer;
}

.dataChat{
    position: absolute;
    left: 65%;
    font-size: 19px;
    top: 1%;
}

.notific{
    position: absolute;
    left: 94%;
    width: 2%;
    height: 20%;
    top: 44%;
    border-radius: 50%;
    background-color: #00A0FF;
    box-shadow: 0px 0px 15px #000FFF;
}

a:visited {
    color: darkgray;
}

.nomeUsuario{
    text-align: center;
    position: relative;
}

.mensagemRec{
    border-radius: 10px;
    background-color: lightgray;
    padding: 10px;
    width: 40%;
    top: 8%;
    position: relative;
    margin-top: 10px;
}

.mensagemEnv{
    border-radius: 10px;
    background-color: #AFAFAF;
    padding: 10px;
    width: 40%;
    top: 8%;
    left: 60%;
    position: relative;
    margin-top: 10px;   
}

.horario{
    position: absolute;
    left: 73%;
    font-size: 13px;
    top: 38%;
}

.buttonEnviar {
  background-color: white;
  color: black;
  border: 3px solid #f44336;
  transition-duration: 0.4s;
  border-radius: 8px;
  padding: 20px 10px;
  text-align: center;
  font-size: 17px;
  display: inline-block;
  font-family: Verdana;
  font-weight: 600;
  position: absolute;
  top: 77.8%;
  left: 82%;
}
.buttonEnviar:hover {
  background-color: #f44336;
  color: white;
  cursor: pointer;
}


.caixaPedidoA{

    border: 3px solid #00FF0F;
    font-family: Arial;
    border-radius: 10px;
    padding: 30px;
    margin-top: 25px;
    width: 23%;
    height: 70%;
    left: 2%;
    position: absolute;
    margin-bottom: 25px;
}

.caixaPedidoB{

    border: 3px solid #008FFF;
    font-family: Arial;
    border-radius: 10px;
    padding: 30px;
    margin-top: 25px;
    width: 23%;
    height: 70%;
    left: 26%;
    position: absolute;
    margin-bottom: 25px;
}


.caixaPedidoC{

    border: 4px solid #FFFF00;
    font-family: Arial;
    border-radius: 10px;
    padding: 30px;
    margin-top: 25px;
    width: 23%;
    height: 70%;
    left: 50%;
    position: absolute;
    margin-bottom: 25px;
}

.caixaPedidoD{

    border: 3px solid #f44336;
    font-family: Arial;
    border-radius: 10px;
    padding: 30px;
    margin-top: 25px;
    width: 23%;
    height: 70%;
    left: 74%;
    position: absolute;
    margin-bottom: 25px;

}

.Pedido{
    position: relative;
    transition: 0.8s;
    left: 1%;
    border: 1px solid #DEDEDE;  
    padding: 3px;
    margin: 6px;
}

.Pedido:hover{
    box-shadow: 10px 10px 20px darkgray;
    width: 105%;
    cursor: pointer;
}

.textP{
    position: relative;
    left: 1%;
    font-size: 15px;
    top: 1%;
}

.dataP{
    position: relative;
    left: 1%;
    font-size: 15px;
    top: 1%;
}

.caixaCompraA{

    border: 3px solid #00FF0F;
    font-family: Arial;
    border-radius: 10px;
    padding: 30px;
    margin-top: 25px;
    width: 23%;
    height: 70%;
    left: 26%;
    position: absolute;
    margin-bottom: 25px;
}

.caixaCompraB{

    border: 3px solid #008FFF;
    font-family: Arial;
    border-radius: 10px;
    padding: 30px;
    margin-top: 25px;
    width: 23%;
    height: 70%;
    left: 50%;
    position: absolute;
    margin-bottom: 25px;
}

.textdestCompra{
    position: absolute;
    top: 19%;
    left: 38%;
    text-shadow: 2px 2px #EEEEEE;

}


.textName{
    position: absolute;
    left: 10%;
    font-size: 19px;
    top: 1%;
}

.dataChat{
    position: absolute;
    left: 65%;
    font-size: 19px;
    top: 1%;
}
.menu{
    position: absolute;
    left: 50%;
    top: 6%;
}

.button {
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
}

.button:hover {
  background-color: #f44336;
  color: white;
  cursor: pointer;
}

.search{
    background-color:white;
    border:solid 2px #f44336;
    border-radius:15px;
    position: absolute;
    left: 28%;
    top: 6.5%;
    
}
.formsearch:focus{
    border-radius:12px;
    border:solid 1px #b40306;
}
.formsearch{
  float:left;
  background-color:transparent;
  padding-left:5px;
  font-style:italic;
  font-size:18px;
  border:none;
  height:32px;
  width:260px;
  transition: 0.5s;
}

#btnBusca{
    cursor: pointer;
}

.divBusca img{
  float:left;
}

.formsearch:focus {
  outline: none

}
.portfolios{
    text-align: center;
    top: 50%;
}

.space{
    height: 40px;
}
.spacetop{
    height: 200px;
}

.dest{
    text-align: center;
    font-family: Verdana;
    font-weight: 800;
    padding: 1px; 
    font-size: 26px;
    background-color: #f44336;
    border-radius: 20px;
    height: 70px;
    border:solid 3px #d40306;

}

.textdest{
    position: absolute;
    top: 19%;
    left: 41%;
    text-shadow: 2px 2px #EEEEEE;
}

.produto{
    height: 320px;
    position: absolute;
    width: 270px;
    border-radius: 10px;
    transition: 0.2s;
    text-align: center;
}

.produto:hover{
    border:solid 3px #f44336;
    cursor: pointer;
}

.titleprod{
    position: relative;
    top: 0%;
    font-family: Verdana;
    font-size: 17px;
    left: 1%;
}

.imgProd{
    position: relative;
    top: 1%;
    padding: 0px;
    left: 1%;
}

.prec{
    font-family: Verdana;
    position: relative;
    top: 1%;
    font-weight: 600;
    font-size: 20px;
    margin-bottom: 15px;
    color: #f40306;
}

button:focus{
    outline: none;
}


a:link {
   color: black;
}

.lupa1{
    transition: 0.2s;
    width: 25px;
}

.lupa1:hover{
    width: 28px;
}


.footer{
    width: 98%;
    background-color: #E2E2E2;
    height: 160px;
    position: absolute;
    top: 150%;
    margin-bottom: 20px;    
    border-radius: 20px;
    text-align: center;
    }

.redes{
    transition: 0.5s;
}
.redes:hover{
    width: 40px;
}
.button2 {
  background-color: white;
  color: black;
  border: 3px solid #00FF0A;
  transition-duration: 0.4s;
  border-radius: 8px;
  padding: 10px 32px;
  text-align: center;
  font-size: 13px;
  display: inline-block;
  font-family: Verdana;
  font-weight: 500;
}

.button2:hover {
  background-color: #00FF0A;
  color: white;
  cursor: pointer;
}
    </style>
</head>

<body>
    <header>
    <div>
        <a href="..\index.html"><img src="..\logo.png" alt="Logo da empresa Axou." width="120" style="margin-top: 0%; cursor: pointer; left: 7%; position: absolute;"></a>

        <div class="menu">
            <a href="Perfil.html"><button class="button">MEUS PRODUTOS</button></a>
            <a href="pedidos.html"><button class="button">PEDIDOS</button></a>
            <a href="Chat.html"><button class="button">CHAT</button></a>
            <a href="visuperfil.html"><div class="button">
                <img class="imguser" src="user.png" alt="Usuário" width="20px"> USUÁRIO</div>
            </div></a>
        	<a href="..\index.html"><button class="button" style="padding: 10px; position: absolute; left: 93.4%; top: 6%; border-radius: 35%;">SAIR</button></a>
        <div class="search">
            <input type="text" id="lname" name="lname" class="formsearch" placeholder="Buscar...">
            <a href="..\Busca\busca.html" class="lupa"><img src="..\LupaPesquisa.png" id="btnBusca" alt="Buscar" class="lupa1"></a>
     </div>

        
        
    </div>
</header>

<div id="main">
    <article>
    	<div class="dest">
    		<h1 class="textdestChat">CHAT</h1>
        </div>


    	<div class="caixaChat">
    			
    		<a href="ChatMensagem1.html"><div class="mensagem">
    			
    			<img src="user.png" class="user-img">
    			<p class="textName" style="top: 1%;"> [nome do usuário]</p>
    			<p class="dataChat">[00:00||00/00]</p>
    			<div class="notific"><p></p></div>

    		</div></a>


    		<a href="ChatMensagem2.html"><div class="mensagem">
    			
    			<img src="user.png" class="user-img">
    			<p class="textName"> [nome do usuário]</p>
    			<p class="dataChat">[00:00||00/00]</p>

    		</div></a>


    		<a href="ChatMensagem2.html"><div class="mensagem">
    			
    			<img src="user.png" class="user-img">
    			<p class="textName"> [nome do usuário]</p>
    			<p class="dataChat">[00:00||00/00]</p>

    		</div></a>
    		<a href="ChatMensagem2.html"><div class="mensagem">
    			
    			<img src="user.png" class="user-img">
    			<p class="textName"> [nome do usuário]</p>
    			<p class="dataChat">[00:00||00/00]</p>

    		</div></a>

    	</div>



    </article>
    <footer>
      <div class="footer">
        
        
        
        <p><a href="https://www.facebook.com/AxouBrasil/?ref=br_rs"><img src="..\iconFace.png" width="35px;" class="redes"></a>  <a href=""><img src="..\iconInsta.png" width="35px;"class="redes"></a> <a href=""><img src="..\iconTwitter.png" width="35px;"class="redes"></a></p>

        <p>B2W - Companhia Digital / CNPJ: 00.000.000/0000-00 / Inscrição Estadual: 00.000.00-0 / Endereço Rua Unoeste, 000 - Presidente Prudente, SP - 18000-000. </p>
        <p>Desde 2020/2 - Contato: <a href="">desenvolvedores@axou.com</a></p>
      </div>
</footer>
</body>
</html>
            '''
        return html



