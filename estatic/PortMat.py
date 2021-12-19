import cherrypy
from PagProduto import *
import os
import sqlite3


class portmat:
    @cherrypy.expose
    def index(self):
        html = '''
        <!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="utf-8"/>
	<title>Portfolio</title>
	<link rel="stylesheet" href="portfolio.css"/>
	<style type="text/css">
		*{background-color:#d3d3d3;}
		.cab{text-align:center;
			 color:white;
			 font-family:Lucida Bright;
			 font-size:50px;
			 }
		#apre{width:63%;
			height:300px;
			float:right;
			font-family:Tw Cen MT;
			font-size:25px;}
		.bordA{border-radius:25px;
			   border:1px solid black;}
	    #pos{position: absolute; 
			left: 45px; 
			top: 620px;}
			dl dt{font-weight:bold;
	  font-size:20px;}
.ttl{font-size:35px; 
text-decoration:underline;}

p{font-size:18px;}
	</style>
</head>
<body>
	<h1 class="cab">MEU PORTFOLIO</h1>
	<hr color="white"/>
	<br/>
	<br/>
    <div >
		<div style="float:left;">
			<figure>
				<img class="bordA" src="eu.jpg" alt="Eu"/>
				<figcaption style="text-decoration:line-through;">foto meio informal mas ta valendo kk</figcaption>
			</figure>
		</div>
	</div>
	<div>
		<div id="apre"><br/>Nome: Mateus Bonassa Ederli<br/>Idade: 18 anos<br/>Formação: Cursando ensino superior<br/>Curso(s) Profissionalizante(s): Inglês<br/>Moro atualmente  em Presidente Prudente - SP e curso Sistema de Informação na Unoeste<br/><br/>No meu tempo de lazer costumo ler,escutar musica,jogar games e assistir futebol,ao menos durante a atual quarentena<br/><br/>
		<em style="text-decoration:underline;">Experiências:</em><br/>Ainda não possuo experiências de trabalho relacionado com a área que curso (Sistemas de Informação), porém já fiz "trabalhos" não remunerados como tradutor na internet durante um tempo </div>
	</div>
	<div id="pos">
		<br/>
		<h3 class="ttl"><em>GOSTOS PESSOAIS</em></h3>
		<dl>
			<dt>Musica</dt>
				<dd>Curto bastante Rap/Trap (Cultura Hip-hop) no geral, escuto Rock e alguns outros gêneros também mas com menor frequência.<br/>
				Além disso,costumo escutar muito Lo-fi enquanto estudo ou programo.</dd>
			<dt>Esporte</dt>
				<dd>Acompanho bastante futebol mas gosto de outros esportes também,como Vôlei e Basquete.<br/>
				No futebol torço para o Santos,mas assisto vários jogos fora os do meu time,principalmente de futebol europeu</dd>
		</dl>
		<br/>
		<h3 class="ttl">Cursos</h3>
		<p>Eu curso atualmente inglês na Legacy (era Yazigi até recentemente) e estou já no ultimo semestre,considero que tenho um nivel muito bom na lingua inglesa.<br/>
		Eu já cheguei a começar a estudar espanhol e japonês também por intermedio de cursos gratuitos e apps online mas acabei não continuando, porém pretendo um dia voltar a me focar em ao menos uma dessas duas linguas.<br/>
		Eu já fiz também "mini-cursos" de desenvolvimento de app e de jogos,porém foi algo bem curto e simples,mas creio que vale a citação.</p>
		<div style="text-align:center;">
			<img src="yazigi.jpg" alt="yazigi" width="640" height="410"/>
		</div>
		<br/>
		<br/>
		<h3 class="ttl">Escolaridade</h3>
		<p>Eu estudei no colegio "Gente Inocente",o qual o nome mudou e atualmente é conhecido como Colegio Prudente,do primário até o quinto-ano,após isso passei a estudar no colégio JP,onde fiquei até me formar.<br/>Atualmente curso BSI na Unoeste.</p>
		<div style="text-align:center;">
			<img src="unoeste.png" alt="unoeste" />
		</div>
		<br/>
		<br/>
	</div>
</body>

</html>
            '''
        return html



