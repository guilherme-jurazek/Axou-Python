import cherrypy
from PagProduto import *
import os
import sqlite3

class ports:
    @cherrypy.expose
    def index(self):
        html = '''
            <!DOCTYPE html>
<html>
<head>
	<title>PORTFOLIOS</title>
	<link rel="stylesheet" type="text/css" href="css.css"/>
	<style type="text/css">.menu{
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
}</style>
</head>
<body>

	<div class="spacetop"></div>

	<div class="portfolios">
	  		<a href="/portgui/"><button class="button">GUILHERME JURAZEK GUEDES</button></a>
  	</div>

	<div class="space"></div>

  	<div class="portfolios">
  		<a href="/portjoao/"><button class="button">JO??O VITOR NUNES ROS GARRIDO</button></a>
  	</div>
  	<div class="space"></div>

  	<div class="portfolios">
		<a href="/portmat/"><button class="button">MATEUS BONASSA EDERLI</button></a>
	</div>	

</body>
</html>'''
        return html



