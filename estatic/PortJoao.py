import cherrypy
from PagProduto import *
import os
import sqlite3


class portjoao:
    @cherrypy.expose
    def index(self):
        html = '''
        <!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="utf-8"/>
	<meta name="description" content="Portifólio João Vitor Garrido"/>

	<title>Portfólio</title>
	<link rel="stylesheet" type="text/css" href="css.css"/>
	<style type="text/css">.texto{
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

	<div class="titulo container2"><img src="EU.jpg" alt="Uma foto minha." class="imagem_rosto"></div>
	<div>
		<h2 class="titulo postitle">PORTIFÓLIO</h2>
		<ul class="info">


			<li>João Vitor Nunes Ros Garrido</li>
			<li>Nascimento: 18/04/2001</li>
			<li>RA: 262013240</li>
			<li>Estudante de Sistemas de Informação - UNOESTE</li>



		</ul>

	</div>
</header>	


<div id='main'>


    <article>

    	<div>
    		<a name="Curso de Informática" id="curso-01"></a>
    		<h3 class="centro titulo">CURSO A+</h3>
    		<p>O meu primeiro curso técnico foi um de informática básica, eu era muito novo e minha mãe fez eu fazer ele para passar o tempo e aprender alguma coisa que poderia ser útil no futuro.</p>
    		
	 		<br>
	 		<br>
	 		<hr>
	 		<br>
	 		<a name="Curso de ingles" id="curso-02"></a>
	 		<h3 class="centro titulo">CURSO DE INGLÊS</h3>	

	 		<p>Fiz muitos anos de curso de inglês. Primeiro em Paraguaçu Paulista onde eu morava e quando iniciei a faculdade em Presidete Prudente continuei o curso na CNA.  </p>
	 		<div class="centro">
	 			<img src="MR.png" alt="Foto da logo do Mr. English." class="imagem_geral" width="450">
			 </div>
			 <div class="centro">
				<img src="cna.jpg" alt="Foto da logo do CNA" class="imagem_geral" width="450">
			</div>
	 		<br>
	 		<br>
	 		<hr>
	 		<br>

	 		<a name="Robotica" id="curso-03"></a>
	 		<h3 class="centro titulo">ROBÓTICA</h3>
	 		<p>A robótica eu comecei a fazer no 9° ano na escola onde eu estudava (SESI) era opcional porém eu me divertia bastante com o lego. Não cheguei a ir no campeonato, fiquei como suplente pois já havia uma equipe montada antes de eu chegar.</p>
	 		<div class="centro">
	 			<img src="LEGO.jpg" alt="única lembrança da época..." class="imagem_geral" width="450">
	 		</div>
	 		<br>
	 		<br>
	 		<hr>
	 		<br>
				 
			 <a name="Arduino" id="curso-04"></a>
	 		<h3 class="centro titulo">ARDUINO</h3>
	 		<p>Ao entrar no colegial nós não tinhamos mais a robótica com lego no SESI e sim o arduino. Foi uma experiência muito bacana, fiz até o 2° ano do ensíno médio e não continuei no #° pois estava mais focado em estudar para os vestibulares. Cheguei a participar de um campeonato mas eu não soube aproveitar pois eu tinha uma ansiedade muito forte e na época eu ainda não fazia tratamento.</p>
	 		<div class="centro">
	 			<img src="ROBO ARD.jpg" alt="Nosso robô do campeonato" class="imagem_geral" width="450">
	 		</div>
	 		<br>
	 		<br>
	 		<hr>
	 		<br>

	 		<a name="Curso de BSI" id="curso-05"></a>
	 		<h3 class="centro titulo">CURSO DE SISTEMAS DE INFORMAÇÃO UNOESTE</h3>	
	 		<p>Iniciei meus estudos no curso de Sistemas de Informação no ano de 2020, na Universidade de Informática do Oeste Paulista(FIPP/UNOESTE). E possuo pretensão de me formar em 2024, desenvolvendo o máximo as minhas habilidades técnicas de programação e análise de sistemas.</p>
	 		<div class="centro">
	 			<a href="https://www.unoeste.br/fipp/"><img src="FIPP.png" alt="Logo da FIPP/UNOESTE." class="imagem_geral" width="450"></a>
	 		</div>
    	</div>

    </article> 


    <nav>
    	<ul style="line-height: 50px;">
    		<li><a href="#curso-01" style="color: black;">Curso A+</a></li>
    		<li><a href="#curso-02" style="color: black;">Curso de Inglês</a></li>
			<li><a href="#curso-03" style="color: black;">Robótica</a></li>
			<li><a href="#curso-04" style="color: black;">Arduino</a></li>
    		<li><a href="#curso-05" style="color: black;">Curso de BSI</a></li>
    	</ul>
    	<p style="margin-top: 3000px"><a href="#topo" style="color: black;" class="topo">Topo</a></p>
    </nav>


 </div>

 



</body>
</html>
            '''
        return html



