import cherrypy
import os
import sqlite3
from css import css
from home import *
local_dir = os.path.dirname(__file__)


class PagProd:

    __id = 0

    def set_id(self, idProd):
        if idProd != "":
            self.__id = idProd

    @cherrypy.expose
    def index(self):

        html = '''
            <!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="utf-8"/>
	<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
	<link rel="stylesheet" type="text/css" href="/css/"/>
	<link rel="stylesheet" type="text/css" href="/csspag/"/>
	
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
    .pag-titleprod{
	position: absolute;
	top: 28%;
	font-family: Verdana;
	font-size: 30px;
	left: 47%;
	font-weight: 700;
}

.pag-prec{
	font-family: Verdana;
	position: absolute;
	top: 55%%;
	left: 47%;
	font-weight: 600;
	font-size: 32px;
	margin-bottom: 15px;
	color: #f40306;
}

.pag-imgProd{
	transition: 0.5s;
}

.pag-imgProd:hover{
	width: 480px;
	box-shadow: 10px 15px 20px black;
}

.pag-imgProdM{
	transition: 0.5s;
}
.pag-imgProdM:hover{
	width: 440px;
	box-shadow: 10px 15px 20px black;
}
.pag-imgProdMM{
	transition: 0.5s;
}
.pag-imgProdMM:hover{
	width: 420px;
	box-shadow: 10px 15px 20px black;
}

.pag-imgProdMMM{
	transition: 0.5s;
}
.pag-imgProdMMM:hover{
	width: 380px;
	box-shadow: 10px 15px 20px black;
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
.pag-cor{
	position: absolute;
	top: 36%;
	font-family: Verdana;
	font-size: 25px;
	left: 47%;
	font-weight: 500;
}

.corProd{
	border-radius: 8px;
	border:solid 2px #f44336;
	width: 32px;
	height: 35px;
	text-align: center;
	position: absolute;
	transition: 0.5s;
}

.corProd:hover{
	width: 35px;
}

.corBox{
	width: 100%;
  	height: 100%;
  	object-fit: fill;
  	border-radius: 6px;
  	transition: 0.5s;
}

.corTxt{
	position: absolute;
	font-family: Verdana;
	font-size: 20px;
	font-weight: 500;
}

.corProd:hover{
	cursor: pointer;
}



.desc{
	text-align: center;
	font-family: Verdana;
  	font-weight: 800;
  	background-color: #f44336;
  	border-radius: 20px;
  	height: 70px;
  	border:solid 3px #d40306;
  	position: absolute;
  	top: 100%;
  	width: 95%;

}

.textdesc{
	position: absolute;
	top: 0%;
	left: 41%;
	font-size: 26px;
	text-shadow: 2px 2px #EEEEEE;
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

.VendedorNome:hover{
	text-decoration: underline;
}
	</style>


</head>

<body>
  <header>


  	<div>
  		<a href=""><img src="https://uploaddeimagens.com.br/images/002/977/642/full/logo.png?1606241516" alt="Logo da empresa Axou." width="100" style="margin-top: 0%%; cursor: pointer; left: 7%%; position: absolute;"></a>

  		<div class="menu">
	  		<a href=""><button class="button">DESTAQUES</button></a>
	  		<a href="Categorias\ca qtegorias.html"><button class="button">PRODUTOS</button></a>
	  		<a href="/login/"><button class="button">MINHA CONTA</button></a>
	  		<a href="portfolios.html"><button class="button">PORTFÓLIOS</button></a>
  		</div>
  		<div class="search">
  				<input type="text" id="lname" name="lname" class="formsearch" placeholder="Buscar...">
  				<a href="Busca\busca.html" class="lupa"><img src="https://uploaddeimagens.com.br/images/002/977/646/full/LupaPesquisa.png?1606241572" id="btnBusca" alt="Buscar" class="lupa1"></a>
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
        html += self.MontarPagProduto()
        html += '''
    	</div>
    </article>
  </div>
  <footer>
	  <div class="footer">



	  	<p><a href="https://www.facebook.com/AxouBrasil/?ref=br_rs"><img src="https://uploaddeimagens.com.br/images/002/977/651/full/iconFace.png?1606241634" width="35px;" class="redes"></a>  <a href=""><img src="https://uploaddeimagens.com.br/images/002/977/652/full/iconInsta.png?1606241648" width="35px;"class="redes"></a> <a href=""><img src="https://uploaddeimagens.com.br/images/002/977/653/full/iconTwitter.png?1606241663" width="35px;"class="redes"></a></p>

	  	<p>B2W - Companhia Digital / CNPJ: 00.000.000/0000-00 / Inscrição Estadual: 00.000.00-0 / Endereço Rua Unoeste, 000 - Presidente Prudente, SP - 18000-000. </p>
	  	<p>Desde 2020/2 - Contato: <a href="">desenvolvedores@axou.com</a></p>
	  </div>
</footer>
</body>'''
        return html


    def MontarPagProduto(self):
        con = sqlite3.connect('BDSite.db')
        cur = con.cursor()
        cur.execute('Select ProdCod, Nome, Preco, Foto, Descricao, Vendedor from Produtos where ProdCod = 1' )
        dados = cur.fetchall()  # recupera os dados do BD em uma lista
        con = sqlite3.connect('BDSite.db')
        cur = con.cursor()
        cur.execute('Select Nome from Usuarios where UserCod = %s' % str(dados[0][5]))
        dados2 = cur.fetchall()  # recupera os dados do BD em uma lista
        html = '''
                
  <div id="main">
    <article>


    	<div>
	    	<div class="pag-produto">
	    		<img src="%s" width="440px;" class="pag-imgProd" style="position: absolute; left: 8%%;">
	    		<a href="/ppp/"><p style="position: absolute; top: 31%%; font-family: Verdana; font-size: 20px; left: 47%%; font-weight: 500;" class="VendedorNome">%s</p></a>
	    		<p class="pag-titleprod" style="top: 33%%">%s</p>
	    		<p class="pag-cor" style="top: 40%%">Qual Cor?</p>
	    		<div class="corProd corBranca" style="top: 55%%; left: 47%%; "></div>
	    		<div class="corProd" style="top: 49%%; left: 47%%;background-color: black;"></div>
	    		<p class="corTxt" style="left: 50%%; top: 47%%;">Preto</p>
	    		<p class="corTxt" style="left: 50%%; top: 53%%;">Branco</p>
	    		<p class="pag-prec"style="top: 56%%">R$%s</p>
	    		<a href="/Pagamento/"><button class="button" style="position: absolute; top: 68%%; left: 47%%; font-size: 20px; font-weight: 600">COMPRAR</button></a>
	    		<a href="..\Comprar\loginChat.html"><button class="button2" style="position: absolute; top: 76%%; left: 47%%; font-size: 15px; font-weight: 550">Enviar mensagem ao vendedor.</button></a>
	    	</div>	
	    	

	    	<div>
		    	<div class="desc" style="top:95%%">
	    			<h1 class="textdesc" style="top:-10%%;">DESCRIÇÃO</h1>
		    	</div>
		    	<div style="position: absolute; top: 105%%; padding: 15px; font-size: 20px; font-family: arial; width: 97%%;">
		    		<p>
		    		%s
					</p>
					<hr>
		    	</div>
			</div>
</article></div>
		
    	
    ''' % (dados[0][3], dados2[0][0], dados[0][1], dados[0][2], dados[0][4])

        return html


local_config = {
    '/':{'tools.staticdir.on':True, 'tools.staticdir.dir':local_dir},
}
config=local_config






