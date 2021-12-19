import cherrypy
from PagProduto import *
import os
import sqlite3


class portgui:
    @cherrypy.expose
    def index(self):
        html = '''
        <!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="utf-8"/>
	<meta name="description" content="Portfólio Guilherme Jurazek Guedes"/>

	<title>Portfólio</title>
	<link rel="stylesheet" type="text/css" href="css.css"/>
	<style type="text/css">
		.texto{
	color: black;
	font-size: 25px;	
	line-height:26px;
	text-indent:50px;
	text-align: justify;
}

.titulo{
	font-weight: bold;
	font-family: arial black;
	text-shadow: 8px 6px 8px darkgray;
}

p{
	padding: 10px;
	text-indent: 25px;
	text-align: justify;
}
.centro{
	text-align: center;
}
.postitle{
	margin-top: 0.5vw;
	text-align: center;
}
.centro img{
	border-radius: 5px;
	border: 3px solid #A3A3A3;
}

.background{
	background-color: #D3D3D3;
}



.tabela{
	text-align: center;
	width: 45%;
	margin: 0 auto;
	color: black;
	font-family: "arial black";

}

.borda td{
	border-color: #D3D3D3;
	margin: 0 auto;
}

.container2{
	border: 1px solid black;
    width: 11.5%;
    height: 28.5%;
    position: absolute;
    text-align: center;
    border-radius: 10px;
}
.imagem_rosto{
	width: 100%;
  	height: 100%;
  	object-fit: fill;
  	border-radius: 10px;

}

.info{
	margin-left: 12%;
	font-size: 20px;
}

body {
   font: 24px Helvetica;
   background: #D3D3D3;
  }



#main {
min-height: 800px;
margin: 0px;
padding: 0px;
display: -webkit-flex;
-webkit-flex-flow: row;
       flex-flow: row;
}

#main > article {
margin: 4px;
padding: 5px;
border: 1px solid #B3B3B3;
border-radius: 7pt;
background: #D3D3D3;
-webkit-flex: 3 1 60%;
       flex: 3 1 60%;
-webkit-order: 2;
       order: 2;
}

#main > nav {
margin: 4px;
padding: 5px;
border: 1px solid #B3B3B3;
border-radius: 7pt;
background: #C3C3C3;
-webkit-flex: 1 6 16%;
       flex: 1 6 16%;
-webkit-order: 1;
       order: 1;
}

header, footer {
display: block;
margin: 4px;
padding: 5px;
min-height: 200px;
border: 1px solid #B3B3B3;
border-radius: 7pt;
background: #C3C3C3;
}


@media all and (max-width: 640px) {

#main, #page {
-webkit-flex-flow: column;
        flex-flow: column;
}

#main > article, #main > nav{

-webkit-order: 0;
        order: 0;
}

#main > nav, #main > aside, header, footer {
min-height: 50px;
max-height: 50px;
}


.imagem_geral{
	width: 50px;
  	height: 100%; 
  	border-radius: 5px;

}

.tabela_desenho{
	margin-left: 10%;
}



.topo{
	margin-bottom: 1%;
	position: absolute;
}
		
	</style>

</head>
<body class="background">
<a name="Topo" id="topo"></a>
<header>

	<div class="titulo container2"><img src="fotorosto.png" alt="Ilustração do meu rosto." class="imagem_rosto"></div>
	<div>
		<h2 class="titulo postitle">PORTFOLIO</h2>
		<ul class="info">


			<li>Guilherme Jurazek Guedes</li>
			<li>Nascimento: 03/01/2002</li>
			<li>RA: 262012677</li>
			<li>Estudante de Sistemas de Informação - UNOESTE</li>



		</ul>

	</div>
</header>	


<div id='main'>


    <article>

    	<div>
    		<a name="Curso de desenho" id="curso-01"></a>
    		<h3 class="centro titulo">CURSO EBAC</h3>
    		<p>Um dos meus primeiros cursos foi o de desenho e ilustrações artísticas. Na Escola Ebac Cursos Profissionalizantes, com o professor Helio Gomes. Iniciei meus estudos na área em 2015, e finalizei em 2017 com o certificado de conclusão. Dentro desses anos eu adquiri bastante experiência em técnicas de ilustrãção, e o básico de perspectiva.</p>
    		<div class="tabela_desenho">
	 			<table class="centro borda" width="100%">
	 				<tr>
	 					<td><img src="Desenho-01.jpg" alt="Desenho com técnicas de realismo." class="imagem_geral" width="400"></td>
	 					<td><img src="Desenho-02.jpg" alt="Desenho com técnicas de realismo e a caneta." class="imagem_geral" width="400"></td>
	 				</tr>
	 				<tr>
	 					<td><img src="Desenho-03.jpg" alt="Desenho com técnicas de rachurado." class="imagem_geral" width="450"></td>
	 					<td><img src="Desenho-04.jpg" alt="Ilustração da capa do jogo scratch do projeto de ambientes." class="imagem_geral" width="480"> </td>
	 				</tr>

	 			</table>
	 		</div>
	 		<br>
	 		<br>
	 		<hr>
	 		<br>
	 		<a name="Curso de dança" id="curso-02"></a>
	 		<h3 class="centro titulo">CURSO DE DANÇA</h3>	

	 		<p>Iniciei um curso de dança em 2017 e saí em 2018 com dois certificados. O objetivo do curso era melhorar a minha habilidade de comunicação e relação interpessoal. Eu sempre fui alguém tímido e tinha como foco quebrar essa barreira, e diante disso me apresentei em dois espetáculos diferentes, com os grupos FIC e Work.</p>
	 		<div class="centro">
	 			<img src="Dança-01.jpg" alt="Foto ilustrando eu no palco." class="imagem_geral" width="450">
	 		</div>
	 		<br>
	 		<br>
	 		<hr>
	 		<br>

	 		<a name="Curso de robótica" id="curso-03"></a>
	 		<h3 class="centro titulo">CURSO DE ROBÓTICA</h3>
	 		<p>Realizei o curso de robótica oferecido pela Toledo Prudente, em parceria com a Inova Prudente em 2019. Foram dois meses de curso onde conheci um pouco de robótica Lego, e programação. Nesse curso entendi melhor como eram feitos e montados robôs lego, e a forma como são programados.</p>
	 		<div class="centro">
	 			<img src="Robo-01.jpg" alt="Foto de um robô que fizemos no curso." class="imagem_geral" width="450">
	 		</div>
	 		<br>
	 		<br>
	 		<hr>
	 		<br>

	 		<a name="Curso de BSI" id="curso-04"></a>
	 		<h3 class="centro titulo">CURSO DE SISTEMAS DE INFORMAÇÃO UNOESTE</h3>	
	 		<p>Iniciei meus estudos no curso de Sistemas de Informação no ano de 2020, na Universidade de Informática do Oeste Paulista(FIPP/UNOESTE). E possuo pretensão de me formar em 2024, desenvolvendo o máximo as minhas habilidades técnicas de programação e análise de sistemas.</p>
	 		<div class="centro">
	 			<a href="https://www.unoeste.br/fipp/"><img src="FIPP.png" alt="Logo da FIPP/UNOESTE." class="imagem_geral" width="450"></a>
	 		</div>
    	</div>

    </article> 


    <nav>
    	<ul style="line-height: 50px;">
    		<li><a href="#curso-01" style="color: black;">Curso de Desenho</a></li>
    		<li><a href="#curso-02" style="color: black;">Curso de Dança</a></li>
    		<li><a href="#curso-03" style="color: black;">Curso de Robótica</a></li>
    		<li><a href="#curso-04" style="color: black;">Curso de BSI</a></li>
    	</ul>
    	<p style="margin-top: 3000px"><a href="#topo" style="color: black;" class="topo">Topo</a></p>
    </nav>


 </div>

 



</body>
</html>
            '''
        return html



