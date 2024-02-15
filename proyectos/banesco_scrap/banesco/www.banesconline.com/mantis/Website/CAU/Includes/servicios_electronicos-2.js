//URL PRODUCCION
var sURLBOL = "https://www.banesconline.com/mantis/"
var sURLPE = "https://pagoelectronico.banesco.com/"
var sURLFI = "https://www.banesconline.com/SIF/"
var sURLBCOM_SE="https://www.banesco.com/"
var sURLCC = "https://www.banesconline.com/SIF/"

var sURLDEMO = "https://www.banesconline.com/mantis/"
var sURLDEMOPE = "https://pagoelectronico.banesco.com/"
var sURLDEMOFI = "https://www.banesconline.com/SIF_Demo/"
var sURLDEMOCAU = "https://www.banesconline.com/mantis/CAU/"
var sURLDEMOCO = "https://www.banesconline.com/CAU_Demo/"
var sURLDEMOETK = "https://www.efecticket.com/ETK_Demo/"
var sURLDEMOPTUR = "https://www.banesconline.com/mantis/CAU/"

function winopendemoPE()
{
	var Ancho = screen.availWidth - 10;
	var Alto = screen.availHeight - 45;
	var sPath = "demo/";
	var features = "toolbar=no,status=yes,directories=no,menubar=no,scrollbars=auto,top=0,left=0,width=" + Ancho + ",height=" + Alto + '"';
	myWindow = window.open(sURLDEMOPE + sPath, "contenido", features);
}
function winopendemoBOL()
{
	var Ancho = screen.availWidth - 10;
	var Alto = screen.availHeight - 45;
	var sPath = "indexlogin_mantis.htm?apli=BOL";
	var features="toolbar=no,status=yes,directories=no,menubar=no,scrollbars=yes,top=0,left=0,width="+Ancho+",height="+Alto+'"';
	myWindow = window.open(sURLDEMOCAU + sPath, "contenido", features);
}
function winopendemoCC()
{
	var Ancho = screen.availWidth - 10;
	var Alto = screen.availHeight - 45;
	var sPath = sURLDEMOCO + "TipoUsuarioGes.htm";
	var features = "toolbar=no,status=yes,directories=no,menubar=no,scrollbars=auto,top=0,left=0,width=" + Ancho + ",height=" + Alto + '"';
	myWindow = window.open(sPath, "contenido", features);
}
function winopendemoFI()
{
	var Ancho = screen.availWidth - 10;
	var Alto = screen.availHeight - 45;
	var sPath = "indexlogin_sif.htm";
	var features = "toolbar=no,status=yes,directories=no,menubar=no,scrollbars=auto,top=0,left=0,width=" + Ancho + ",height=" + Alto + '"';
	myWindow = window.open(sURLDEMOCAU + sPath, "contenido", features);
}
function winopendemoETK()
{
	var Ancho = screen.availWidth - 10;
	var Alto = screen.availHeight - 45;
	var sPath = "Pagina.htm";
	var features = "toolbar=no,status=yes,directories=no,menubar=no,scrollbars=auto,top=0,left=0,width=" + Ancho + ",height=" + Alto + '"';
	myWindow = window.open(sURLDEMOETK + sPath, "contenido", features);
}
function winopendemoBC()
{
	var Ancho = screen.availWidth - 10;
	var Alto = screen.availHeight - 45;
	var sPath = "Pagina.htm";
	var features = "toolbar=no,status=yes,directories=no,menubar=no,scrollbars=auto,top=0,left=0,width=" + Ancho + ",height=" + Alto + '"';
	myWindow = window.open(sURLDEMOBC + sPath, "contenido", features);
}
function winopendemoTUR()
{
	var Ancho = screen.availWidth - 10;
	var Alto = screen.availHeight - 45;
	var sPath = "indexlogin_ptur.htm?apli=BOL";
	var features="toolbar=no,status=yes,directories=no,menubar=no,scrollbars=yes,top=0,left=0,width="+Ancho+",height="+Alto+'"';
	myWindow = window.open(sURLDEMOPTUR + sPath, "contenido", features);
}
