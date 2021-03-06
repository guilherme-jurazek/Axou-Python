import cherrypy


class csspag:
    @cherrypy.expose
    def index(self):
        return '''
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
	width: 500px;
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
} '''
