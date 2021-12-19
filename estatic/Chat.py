import cherrypy
from PagProduto import *
import os
import sqlite3


class chat:
    @cherrypy.expose
    def index(self):
        html = '''
        <!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="utf-8"/>
	<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
	<link rel="stylesheet" type="text/css" href="..\css.css"/>
	<link rel="stylesheet" type="text/css" href="cssChat.css"/>
	<title>Axou</title>	
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
.search{
	background-color:white;
  	border:solid 2px #f44336;
  	border-radius:15px;
	position: absolute;
	left: 28%;
	top: 6.5%;
	
}
.formchat:focus{
	border-radius:12px;
	border:solid 1px #b40306;
}
.formchat{
  padding-left:5px;
  font-style:italic;
  font-size:18px;
  border:none;
  height:32px;
  width:60%;
  transition: 0.5s;
}

#btnEnviar{
	cursor: pointer;
}

.divBusca img{
  float:left;
}

.formchat:focus {
  outline: none

}
.enviar{
	width: 30px;
}

.buttonEnviar {
  background-color: white;
  color: black;
  border: 3px solid #f44336;
  transition-duration: 0.4s;
  border-radius: 8px;
  padding: 10px 32px;
  text-align: center;
  font-size: 18px;
  display: inline-block;
  font-family: Verdana;
  font-weight: 600;
  position: absolute;
  top: 70%;
  left: 46%;
}

.buttonEnviar:hover {
  background-color: #f44336;
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
	  		<a href="..\index.html"><button class="button">DESTAQUES</button></a>
	  		<a href="..\Categorias\categorias.html"><button class="button">PRODUTOS</button></a>
	  		<a href="..\loginreg\login.html"><button class="button">MINHA CONTA</button></a>
	  		<a href="..\portfolios.html"><button class="button">PORTFÓLIOS</button></a>
  		</div>
  		<div class="search">
  				<input type="text" id="lname" name="lname" class="formsearch" placeholder="Buscar...">
  				<a href="..\Busca\busca.html" class="lupa"><img src="..\LupaPesquisa.png" id="btnBusca" alt="Buscar" class="lupa1"></a>
   		</div>
  		
  	</div>
  	
  	<div>	
  		<div class="chat">
  			<textarea style="float:left; clear:left; position: absolute; left: 34%; top: 33%; width: 500px; font-size: 20px;" name="mensagem" cols="23" rows="10" id="mensagem" [COLOR="Red"]wrap="hard"[/COLOR] placeholder="Escreva aqui a sua mensagem!"></textarea>		
  			<a href="Mensagem.html"><button class="buttonEnviar">ENVIAR</button></a>
   		</div>
   		
  	</div>


  </header>
  
    	
    </article>
  </div>
  <footer>
	  <div class="footer">
	  	
	  	
	  	
	  	<p><a href="https://www.facebook.com/AxouBrasil/?ref=br_rs"><img src="..\iconFace.png" width="35px;" class="redes"></a>  <a href=""><img src="..\iconInsta.png" width="35px;"class="redes"></a> <a href=""><img src="..\iconTwitter.png" width="35px;"class="redes"></a></p>

	  	<p>B2W - Companhia Digital / CNPJ: 00.000.000/0000-00 / Inscrição Estadual: 00.000.00-0 / Endereço Rua Unoeste, 000 - Presidente Prudente, SP - 18000-000. </p>
	  	<p>Desde 2020/2 - Contato: <a href="">desenvolvedores@axou.com</a></p>
	  </div>
</footer>
</body>
            '''
        return html



