import cherrypy
import sqlite3
from home import *
from css import css


class CadProd:
    # propriedades que representam os campos da tabela no BD
    id = 0
    cname = ""
    cnumber = ""
    emonth = ""
    eyear = ""
    cv = ""

    @cherrypy.expose()
    def index(self):
        html = '''
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
        <a href="..\index.html"><img src="https://uploaddeimagens.com.br/images/002/977/642/full/logo.png?1606241516" alt="Logo da empresa Axou." width="120" style="margin-top: 0%; cursor: pointer; left: 7%; position: absolute;"></a>

        <div class="menu">
            <a href="Perfil.html"><button class="button">MEUS PRODUTOS</button></a>
            <a href=""><button class="button">PEDIDOS</button></a>
            <a href="Chat.html"><button class="button">CHAT</button></a>
            <a href=""><div class="button">
                <img class="imguser" src="https://uploaddeimagens.com.br/images/002/988/807/full/user.png?1607021669" alt="Usuário" width="20px"> Usuário</div>
        	</div></a>
       		<a href="..\index.html"><button class="button" style="padding: 10px; position: absolute; left: 93%; top: 6%; border-radius: 35%;">SAIR</button></a>
        <div class="search">
            <input type="text" id="lname" name="lname" class="formsearch" placeholder="Buscar...">
            <a href="" class="lupa"><img src="https://uploaddeimagens.com.br/images/002/977/646/full/LupaPesquisa.png?1606241572" id="btnBusca" alt="Buscar" class="lupa1"></a>
     </div>

        
        
    </div>
</header>
    '''
        html += '''
  
       <div id="main">
    <article>
		<div class="dest">
    		<h1 class="textdest1">Cadastro de produtos</h1>
		</div>
		
		<div class="textLabel">
		<form action="CadProd" method="GET">

			<br/>

			<label for="farq">Selecione a foto do seu Produto:</label>
			<input type="file" id="farq" size="40"/>

			<br/>
			<br/>

			<label for="tprod"> Nome do Produto:</label>
			<input type="text" id="tprod" name="nameprod" size="40" maxlength="30" placeholder="Nome do produto" autofocus="true" required="required" />
			
			<br/><br/>  

			<label for="preco">Preço do produto:</label>
			<input type="text" id="tprod" name="precprod" size="40" maxlength="20" placeholder="R$99,99" autofocus="true" required="required"/>

			<br/><br/>


			<label for="estprod">Estado do produto:</label>
'''
        html += self.carregar_combobox3()
        html+='''
				<br/>
				<br/>
        
				<label for="categoria">Categoria:</label>
        
                '''
        html += self.carregar_combobox1()
        html +=    '''
				
				<br/><br/>

				
        <label for="categoria">Cor:</label>
				'''
        html += self.carregar_combobox2()
        html +='''
				
				<br/><br/>

				<label for="descprod">Descrição do produto:</label><br/>

                <textarea name="desc" type="text" id="descprod" cols="60" rows="15" placeholder="Descrição..." required="required" ></textarea>

				<br/><br/> 
				
				<input type="submit" id="bsalvar" value="Salvar cadastro" style="font-size: 20px;" />
			


	
		</form>
		</div>
		
	</article>
  </div>
  <footer>
</footer>
</body> '''
        return html

    @cherrypy.expose()
    def CadProd(self, nameprod, precprod, condicao, desc, cat, cor):
        con = sqlite3.connect('BDSite.db')
        cur = con.cursor()
        sql = "insert into Produtos (Nome, Preco, Novo, Descricao, CategoriaCod, CodCor1) values ('%s', '%s', '%s', '%s', '%s', '%s') " % (str(nameprod), str(precprod), str(condicao), str(desc), str(cat), str(cor))
        sucesso = True  # indicar que deu certo!!
        try:
            cur.execute(sql)
            con.commit()
        except:
            sucesso = False
        con.close()
        if not sucesso:
            return "<h2>Erro ao cadastrar/alterar Produto!! <a href='/.'> Clique  aqui</a> para retornar ao formulário... </h2>"
        else:
            # precisa inicilizar as propriedades
            raise cherrypy.HTTPRedirect('/.')  # refresh e atualiza a página (como se fosse um F5)

    @cherrypy.expose()
    def carregar_combobox1(self):
        con = sqlite3.connect('BDSite.db')
        cur = con.cursor()
        cur.execute("Select * from Categorias order by NomeCategoria")
        dados = cur.fetchall()
        html = '<select name="cat" >'  # o nome deve ser o mesmo do parâmentro
        for categoria in dados:
                html += '<option value=%s> %s </option> ' % (str(categoria[0]), categoria[1])
        html += '</select>'
        return html

    @cherrypy.expose()
    def carregar_combobox2(self):
        con = sqlite3.connect('BDSite.db')
        cur = con.cursor()
        cur.execute("Select * from Cores order by NomeCor")
        dados = cur.fetchall()
        html = '<select name="cor" >'  # o nome deve ser o mesmo do parâmentro
        for cor in dados:
            html += '<option value=%s> %s </option> ' % (str(cor[0]), cor[1])
        html += '</select>'
        return html

    @cherrypy.expose()
    def carregar_combobox3(self):
        con = sqlite3.connect('BDSite.db')
        cur = con.cursor()
        cur.execute("Select * from Cond order by CodCond")
        dados = cur.fetchall()
        html = '<select name="condicao" >'  # o nome deve ser o mesmo do parâmentro
        for cond in dados:
            html += '<option value=%s> %s </option> ' % (str(cond[0]), cond[1])
        html += '</select>'
        return html