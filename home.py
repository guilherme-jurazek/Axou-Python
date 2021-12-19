import cherrypy

from AdminUser import Admin
from PagProduto import*
import os
import sqlite3
from estatic.Busca import busca
from estatic.Chat import chat
from estatic.Chat2 import chat2
from estatic.duvidas import duvidas
from estatic.Mensagem import mensagem
from estatic.pedidos import pedidos
from estatic.Port import ports
from estatic.PortGui import portgui
from estatic.PortJoao import portjoao
from estatic.PortMat import portmat
from PerfilUsuario import Perfil2
from alterardadosusuario import Alterar
from cadprincipal import CadPrincipal
from css import css
from estilo.csspag import csspag
from Pagamento import Pagamento
from CadProd import CadProd
from AltProd import AltProd
from login import LogPrincipal
from perfilpadrao import PerfilP

local_dir = os.path.dirname(__file__)






class HomePage:
    @cherrypy.expose
    def index(self):
        html = '''
            <!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="utf-8"/>
	<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
	<link rel="stylesheet" type="text/css" href="estilo/css.css"/>
	<title>Axou</title>	
	<style type="text/css" media="screen">
	 	* {
			box-sizing: border-box; 
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
	top: 150%%;
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
		
	</style>


</head>

<body>
  <header>


  	<div>
  		<a href="/home/"><img src="https://uploaddeimagens.com.br/images/002/977/642/full/logo.png?1606241516" alt="Logo da empresa Axou." width="120" style="margin-top: 0%%; cursor: pointer; left: 7%%; position: absolute;"></a>

  		<div class="menu">
	  		<a href=""><button class="button">DESTAQUES</button></a>
	  		<a href=""><button class="button">PRODUTOS</button></a>
	  		<a href="/login/"><button class="button">MINHA CONTA</button></a>
	  		<a href="/ports/"><button class="button">PORTFÓLIOS</button></a>
  		</div>
  		<div class="search">
  				<input type="text" id="lname" name="lname" class="formsearch" placeholder="Buscar...">
  				<a href="/busca/" class="lupa"><img src="https://uploaddeimagens.com.br/images/002/977/646/full/LupaPesquisa.png?1606241572" id="btnBusca" alt="Buscar" class="lupa1"></a>
   		</div>

  		
  		
  	</div>
  	


  </header>
  <div id="main">
    <article>
    	<div class="dest">
    		<h1 class="textdest">DESTAQUES</h1>
    	</div>


    	<div>
	    	
    '''
        html += self.MontarProduto()
        html += '''
    	</div>
    </article>
  </div>
  <footer>
  
	 
</footer>
</body>'''
        return html

    @cherrypy.expose()
    def MontarProduto(self):
        con = sqlite3.connect('BDSite.db')
        cur = con.cursor()
        cur.execute(
            'Select ProdCod, Nome, Preco, Foto from Produtos')
        dados = cur.fetchall()  # recupera os dados do BD em uma lista
        x = 40
        y = 5
        z = 1
        html = ''''''
        for produtos in dados:

            if z == 1:
                y = 5
            elif z == 5:
                z = 1
                x += 55
                y = 5
            html += '''
                <a href="/PagProd/"><div class="produto" style="top: %d%%; left: %d%%;">
                    <img src="%s" width="200px;" height="200px;" class="imgProd">
                    <p class="titleprod">%s</p>
                    <p class="prec">R$%s</p>
                </div></a>''' % (x, y, produtos[3], produtos[1], produtos[2])
            y += 24
            z += 1

        return html


#objetos para cada classe:
root = HomePage()
root.home = HomePage()
root.css = css()
root.css = csspag()
root.PagProd = PagProd()
root.admin = Admin()
root.Pagamento = Pagamento()
root.CadProd = CadProd()
root.AltProd = AltProd()
root.per = Perfil2()
root.cad = CadPrincipal()
root.alt = Alterar()
root.login = LogPrincipal()
root.ppp = PerfilP()


root.busca = busca()
root.chat = chat()
root.chat2 = chat2()
root.duvidas = duvidas()
root.mensagem = mensagem()
root.pedidos = pedidos()
root.ports = ports()
root.portgui = portgui()
root.portjoao = portjoao()
root.portmat = portmat()


local_config = {
    '/':{'tools.staticdir.on':True, 'tools.staticdir.dir':local_dir},
}

cherrypy.quickstart(root, config=local_config)



