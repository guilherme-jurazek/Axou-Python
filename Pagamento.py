import cherrypy
import sqlite3
from home import *
from css import css
class Pagamento:
    # propriedades que representam os campos da tabela no BD
    id = 0
    cname = ""
    cnumber = ""
    emonth = ""
    eyear = ""
    cv = ""
    @cherrypy.expose()
    def index(self):
       html= '''
       <head>
	<meta charset="utf-8"/>
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
		
	.tabela{
	font-family: Arial;
	font-size: 24px;
	text-align: center;
	position: absolute;
	top: 25.5%;
	left: 24%;	
	border: 1px solid black;
	border-radius: 8px;
}
th, td {
  padding: 7px;
}


.container123 {
  padding: 5px 20px 15px 20px;
  border-radius: 3px;
}

.input {
  width: 405px;
  margin-bottom: 20px;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

label {
  margin-bottom: 10px;
  display: block;
}

.icon-container {
  margin-bottom: 20px;
  padding: 7px 0;
  font-size: 24px;
}

.btn {
  background-color: #4CAF50;
  color: white;
  padding: 12px;
  margin: 10px 0;
  border: none;
  width: 200px;
  border-radius: 3px;
  cursor: pointer;
  font-size: 17px;
  transition: 0.2s;
}

.btn:hover {
  background-color: #45a049;
}

.btn2 {
  background-color: #2CA05F;
  color: white;
  padding: 12px;
  margin: 10px 0;
  border: none;
  width: 200px;
  border-radius: 3px;
  cursor: pointer;
  font-size: 17px;
  transition: 0.2s;
}

.btn2:hover {
  background-color: #2C905F;
}

.compra{
	border: 1px solid black;
	border-radius: 8px;	
	padding: 10px;
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


input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

	</style>


</head>
<body>
<header>


  	<div>
  		<a href="/home/"><img src="https://uploaddeimagens.com.br/images/002/977/642/full/logo.png?1606241516" alt="Logo da empresa Axou." width="120" style="margin-top: 0%; cursor: pointer; left: 7%; position: absolute;"></a>

  		<div class="menu">
	  		<a href="..\index.html"><button class="button">DESTAQUES</button></a>
	  		<a href="..\Categorias\categorias.html"><button class="button">PRODUTOS</button></a>
	  		<a href="/login/"><button class="button">MINHA CONTA</button></a>
	  		<a href="..\portfolios.html"><button class="button">PORTFÓLIOS</button></a>
  		</div>
  		<div class="search">
  				<input type="text" id="lname" name="lname" class="formsearch" placeholder="Buscar...">
  				<a href="..\Busca\\busca.html" class="lupa"><img src="https://uploaddeimagens.com.br/images/002/977/646/full/LupaPesquisa.png?1606241572" id="btnBusca" alt="Buscar" class="lupa1"></a>
   		</div>

  		
  		
  	</div>
  	


  </header>
       <div class="position">
            '''
       html += self.MontarTabela()
       html +='''
    		
    		<div style="position: absolute; left: 50%; top: 25%;" class="compra">
			  <div>
			    <div>
			      <form action="cad_compra" method="GET">

			        <div class="">
			            <label for="cname">Nome no Cartão</label>
			            <input type="text" name="cardname" class="input" size="30" required="required"/>
			            <label for="ccnum">Número do Cartão</label>
			            <input type="number" name="cardnumber" class="input"  pattern="\d{4}\s\d{4}\s\d{4}" title="0000 0000 0000 0000" required="required"/>
			            <label for="expmonth">Validade Mês</label>
			            <input type="number" name="expmonth" class="input" value="%s" required="required"/>

			            <div class="">
			              <div class="">
			                <label for="expyear">Validade Ano</label>
			                <input type="number" name="expyear" class="input" value="%s" required="required"/>
			              </div>
			              <div class="">
			                <label for="cvv">CVV</label>
			                <input type="number" name="cvv" class="input" value="%s" required="required"/>
			              </div>
			            </div>
			          </div>

			        </div>
			        <input type="submit" value="Finalizar Compra" class="btn" value="Gravar">
			        <a href="boleto.html"><input type="post" value="Gerar Boleto" class="btn2"></a>
			
			      </form>
			    </div>
			  </div>


			</div>
    	</div>
    	<footer>
	  <div class="footer">
	  	
	  	
	  	
            <p><a href="https://www.facebook.com/AxouBrasil/?ref=br_rs"><img src="https://uploaddeimagens.com.br/images/002/977/651/full/iconFace.png?1606241634" width="35px;" class="redes"></a>  <a href=""><img src="https://uploaddeimagens.com.br/images/002/977/652/full/iconInsta.png?1606241648" width="35px;"class="redes"></a> <a href=""><img src="https://uploaddeimagens.com.br/images/002/977/653/full/iconTwitter.png?1606241663" width="35px;"class="redes"></a></p>
    
            <p>B2W - Companhia Digital / CNPJ: 00.000.000/0000-00 / Inscrição Estadual: 00.000.00-0 / Endereço Rua Unoeste, 000 - Presidente Prudente, SP - 18000-000. </p>
            <p>Desde 2020/2 - Contato: <a href="">desenvolvedores@axou.com</a></p>
	  </div>
</footer>
 </body>   	
       '''
       return html

    @cherrypy.expose()
    def cad_compra(self,cardname, cardnumber, expmonth, expyear, cvv):
        con = sqlite3.connect('BDSite.db')
        cur = con.cursor()
        sql = "insert into Compras (NomeCartao, Cartao, ExpMonth, ExpYear, CVV) values ('%s', %s, %s, %s, %s) " % (cardname, cardnumber, expmonth, expyear, cvv)
        sucesso = True # indicar que deu certo!!
        try:
            cur.execute(sql)
            con.commit()
        except:
            sucesso = False
        con.close()
        if not sucesso:
            return "<h2>Erro ao cadastrar/alterar Cartão!! <a href='/.'> Clique  aqui</a> para retornar ao formulário... </h2>"
        else:
            # precisa inicilizar as propriedades
            self.id = 0
            self.cname = ""
            self.cnumber = ""
            self.emonth = ""
            self.eyear = ""
            self.cv = ""

            raise cherrypy.HTTPRedirect('/.')# refresh e atualiza a página (como se fosse um F5)

    @cherrypy.expose()
    def MontarTabela(self):
        con = sqlite3.connect('BDSite.db')
        cur = con.cursor()
        cur.execute('Select Preco from Produtos where ProdCod = 1')
        dados = cur.fetchall()  # recupera os dados do BD em uma lista
        html = '''
            <div class="tabela" style="font-family: Arial; font-size: 24px; text-align: center; position: absolute; top: 25.5%%; left: 24%%; border: 1px solid black; border-radius: 8px;">
    			<table>
    			<tr> 
    				<td>Valor do Produto: </td>
    				<td>R$ %s</td>
    			</tr>
    			<tr> 
    				<td>Valor do Frete: </td>
    				<td>R$ 00,00</td>
    			</tr>
    			<tr> 
    				<td>Total: </td>
    				<td>R$ %s</td>
    			</tr>
    			</table>
    		</div>''' % (dados[0][0], dados[0][0])
        return html