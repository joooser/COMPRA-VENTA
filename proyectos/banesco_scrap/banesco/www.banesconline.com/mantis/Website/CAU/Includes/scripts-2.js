var nc = (document.layers) ? true : false;
var ie = (document.all) ? true : false;
var n6 = (document.getElementById) ? true : false;
//Bloqueo de Teclas de Funciones + Rigth Click
//document.onkeydown = bloquearTeclasFuncion;
function bloquearTeclasFuncion()
{
	if(window.event)
	{
		if((window.event.keyCode == 8) || ((window.event.keyCode >= 113) && (window.event.keyCode <= 123)))
		{
			window.event.cancelBubble = true;
			window.event.keyCode = 8;
			window.event.returnValue = false;
			return false;
		}
	}
	if(event.altLeft)
		if((window.event.keyCode == 37) || (window.event.keyCode == 39))
			return false;
	if(event.ctrlKey)
		return false;
	return true;
}
function clickIE()
{
	if(ie)
		return false;
	return true;
}
function clickNS(e)
{
	if(nc || (n6 && (!ie)))
		if(e.which == 2 || e.which == 3)
			return false;
	return true;
}

if (nc) {
	document.captureEvents(Event.MOUSEDOWN);
	document.onmousedown = clickNS;
}
else {
	document.onmouseup = clickNS;
	document.oncontextmenu = clickIE;
}

//Fin Bloqueo de Teclas de Funciones + Rigth Click
//Script para desactivar la visualizacion de codigo al producirce un error Java Script 
//Esta libreria debe ser incluida en cada una de las paginas dentro de la etiquetas <head></head>
var oVentanaAyuda;
function detenerError()
{
	return true
}
window.onerror = detenerError
function volver(destino)
{
	document.location.href = destino
}
//----------------------------------------------------------
/*
* Esta función se crea para abrir las ventanas de las ayudas 
* diseñadas durante el 
* proyecto de CVC2. 
*
* Por: David Del Corral
* Fecha: 29-1-2005
*/
function AbrirVentanAyuda(sUrl, Ancho, Alto)
{
	if(oVentanaAyuda != null)
	{
		oVentanaAyuda.close();
		oVentanaAyuda = null;
	}
	var features="toolbar=no,status=no,directories=no,menubar=no,scrollbars=no,left=1,top=130,screenX=1,screenY=130',width="+Ancho+",height="+Alto+'"';
	oVentanaAyuda = window.open(sUrl, 'bol_Ayuda', features);
	oVentanaAyuda.focus();
}
function EsMonto(Str)
{
	var Result;
	Result = TodosEspacios(Str);
	if(Result)
		return false;
	for(var i = 0; i < Str.length; i++)
	{
		if((Str.charCodeAt(i) >= 48 && Str.charCodeAt(i) <= 57) || Str.charAt(i) == "." || Str.charAt(i) == ",")
			continue;
		else
			return false;
	}
	return true;
}
function TodosEspacios(str)
{
	for(var i = 0; i < str.length; i++)
	{
		if(str.charAt(i) == " ")
			continue;
		else
			return false;
	}
	return true;
}
function SuprimirEspacios(str)
{
	var strnew = "";
	for(var i = 0; i < str.length; i++)
	{
		if(str.charAt(i) != " ")
			strnew += str.charAt(i);
	}
	return strnew;
}
function EsNumero(Str)
{
	var Result
	Result = TodosEspacios(Str);
	if(Result)
		return false;
	for(var i = 0; i < Str.length; i++)
	{
		if((Str.charCodeAt(i) >= 48 && Str.charCodeAt(i) <= 57))
			continue;
		else
			return false;
	}
	return true;
}
//Formatea los montos de los Pagos Mínimo y Pago Total
function NormalizarMontosPago(str)
{
	var Monto = "";
	for(var i = 0; i < str.length; i++)
	{
		if(str.charAt(i) == ",")
			Monto += ".";
		else
			if(str.charAt(i) != ".")
				Monto += str.charAt(i);
	}
	return Monto;
}
function CerosyEspacios(str)
{
	for(var i = 0; i < str.length; i++)
	{
		if(str.charAt(i) == "0" || str.charAt(i) == " " || str.charAt(i) == "." || str.charAt(i) == ",");
		else
			return false;
	}
	return true;
}
function ContarCaracter(str, car)
{
	var c = 0;
	var ExisteComa = false;
	var Coma = ",";
	for(var i = 0; i < str.length; i++)
	{
		if(str.charAt(i) == car )
		{
			if(!ExisteComa)
				c++;
		}
		if(str.charAt(i) == Coma)
		{
			c = 0;
			ExisteComa = true;
		}
	}
	return c;
}
//Obtiene la parte entera y Decimal del numero
function ObtenerParteEnterayDecimal(Obj, car)
{
	var str = Obj.Monto;
	var siHayDecimal = false;
	var c = 0;
	ParteEntera = ""
	ParteDecimal = ""
	for(var i = 0; i < str.length; i++)
	{
		if(str.charAt(i) == car)
		{
			siHayDecimal = true;
			if(c == 0)
			{
				c++;
				continue;
			}
		}
		if(siHayDecimal)
			ParteDecimal += str.charAt(i);
		else
			ParteEntera += str.charAt(i);
	}
	Obj.ParteEntera = ParteEntera
	Obj.ParteDecimal = ParteDecimal
	return true;
}
function HayunNumero(Str)
{
	for(var i = 0; i < Str.length; i++)
	{
		if(IsNumero(Str.charAt(i)))
			return true;
	}
	return false;
}
function IsNumero(Str)
{
	if(Str.charCodeAt(0) >= 48 && Str.charCodeAt(0) <= 57)
		return true;
	return false;
}
function TodosNumero(Obj)
{
	var NumerodeDecimales = 0;
	Str = Obj.ParteDecimal
	for(var i = 0; i < Str.length; i++)
	{
		NumerodeDecimales++;
		if(!IsNumero(Str.charAt(i)))
			return false;
	}
	Obj.Decimales = NumerodeDecimales
	return true;
}
function EliminarCerosNoSignificativos(Obj)
{
	var Monto= Obj.ParteEntera;
	var MontoNew = "";
	var CerosIzquierda = true;
	var Ceros = 0;
	if(CerosyEspacios(Monto))
	{
		for(var i = 0; i < Monto.length; i++)
		{
			if(Ceros == 0)
			{
				MontoNew += Monto.charAt(i);
				Ceros++;
			}
			else
				break;
		}
		Obj.ParteEntera = MontoNew;
		return
	}
	for(var i = 0; i < Monto.length; i++)
	{
		if(Monto.charAt(i)== "0" && CerosIzquierda == true)
			continue;
		else
		{
			CerosIzquierda = false;
			MontoNew += Monto.charAt(i);
		}
	}
	Obj.ParteEntera = MontoNew;
}
function AsignardosDecimales(Obj)
{
	var NumeroDecimales = Obj.Decimales;
	var Monto = Obj.ParteDecimal;
	var MontoDecimal = ",";
	if(NumeroDecimales < 2)
	{
		MontoDecimal += Monto;
		for(var i = NumeroDecimales; i < 2; i++)
			MontoDecimal += "0";
	}
	else
	{
		for(var i = 0; i < 2; i++)
			MontoDecimal += Monto.charAt(i);
	}
	Obj.ParteDecimal = MontoDecimal;
}
function FormatearSeparadorMiles(Obj)
{
	var Monto = Obj.ParteEntera;
	var PosMil = 0;
	var Punto= ".";
	var MontoInv = "";
	for(var i = Monto.length - 1; i >= 0; i--)
	{
		if(PosMil == 3)
		{
			PosMil = 1;
			MontoInv += ".";
			if(Monto.charAt(i) == Punto)
				PosMil = 0;
			else
				MontoInv += Monto.charAt(i);
		}
		else
		{
			if(!IsNumero(Monto.charAt(i)))
				return false;
			MontoInv += Monto.charAt(i);
			PosMil++;
		}
	}
	Monto = "";
	for(var i = MontoInv.length - 1; i >= 0; i--)
	{
		Monto += MontoInv.charAt(i);
	}
	Obj.ParteEntera = Monto;
	return true;
}
function ValidarMonto(Obj)
{
	var i, j
	var Monto = Obj.Monto;
	var Result
	var car = ",";
	var Punto= ".";
	if(CerosyEspacios(Monto))
	{
		alert("El monto debe ser mayor que cero.")
		return Obj.Exito;
	}
	if(ContarCaracter(Monto, Punto) == 1)
	{
		car = Punto;
	}
	Result = ObtenerParteEnterayDecimal(Obj, car);
	Result = HayunNumero(Obj.ParteEntera)
	if(!Result)
	{
		alert("Monto incorrecto. Por favor verifique.");
		return Obj.Exito;
	}
	Result = TodosNumero(Obj);
	if(!Result)
	{
		alert("Monto Incorrecto. Utilice un punto (.) para separar las unidades de miles y una coma (,) para los decimales. Ej: 5.650.000,00");
		return Obj.Exito;
	}
	Result = EliminarCerosNoSignificativos(Obj);
	Result = AsignardosDecimales(Obj);
	Result = FormatearSeparadorMiles(Obj);
	if(!Result)
	{
		alert("Monto Incorrecto. Utilice un punto (.) para separar las unidades de miles y una coma (,) para los decimales. Ej: 5.650.000,00");
		return Obj.Exito;
	}
	Obj.Monto = Obj.ParteEntera + Obj.ParteDecimal
	Obj.Exito = true;
	return Obj.Exito;
}
function EsAlphaNumerico(Str)
{
	var Result = TodosEspacios(Str);
	if(Result)
		return false;
	for(var i = 0; i < Str.length; i++)
	{
		if((Str.charCodeAt(i) >= 48 && Str.charCodeAt(i) <= 57) || (Str.charCodeAt(i) >= 65 && Str.charCodeAt(i) <= 90)||(Str.charCodeAt(i) >= 97 && Str.charCodeAt(i) <= 122))
			continue;
		else
			return false;
	}
	return true;
}
function HayEspacio(str)
{
	for(var i = 0; i < str.length; i++)
	{
		if(str.charAt(i) == " ")
			return false;
	}
	return true;
}
function ConvertirFecha(obj)
{
	var d = new Date(obj.yy, obj.mm - 1, obj.dd);
	obj.dd = d.getDate();
	obj.mm = d.getMonth() + 1;
	obj.yy = d.getFullYear();
}
function DateDiff(dd, mm, yy, ddf, mmf, yyf, Accion)
{
	var ddt, mmt, yyt, ddtf, mmtf, yytf;
	var TotalMes = 0;
	var TotalDia = 0;
	var MesActual;
	var d1, d2;
	Accion = Accion.toUpperCase(Accion);
	mm--;
	mmf--;
	d2 = new Date(yyf, mmf, ddf);
	ddtf = d2.getDate();
	mmtf = d2.getMonth();
	yytf = d2.getFullYear();
	while(true)
	{
		d1 = new Date(yy, mm, dd);
		ddt = d1.getDate();
		mmt = d1.getMonth();
		MesActual = mmt;
		yyt = d1.getFullYear();
		if(ddt == ddtf && mmt == mmtf && yyt == yytf)
			break
		TotalDia++;
		d1 = new Date(yyt, mmt, ddt + 1);
		ddt = d1.getDate();
		mmt = d1.getMonth();
		yyt = d1.getFullYear();
		dd = ddt;
		mm = mmt;
		yy = yyt;
		if(mmt != MesActual)
			TotalMes++;
	}
	if(Accion == 'M')
		return TotalMes;
	else
		return TotalDia;
}
function Rellenar(Str, car, n)
{
	var NumeroaRellenar = Math.abs(Str.length - n);
	var Texto = "";
	for(var i = 0; i < NumeroaRellenar; i++)
	{
		Texto += car;
	}
	Texto += Str;
	return Texto;
}
function ReemplazarCaracter(stemp)
{
	myString = new String(stemp);
	rExp = /(\")/gi;
	myString = myString.replace(rExp, " ");
	rExp = /(\')/gi;
	myString = myString.replace(rExp, " ");
	rExp = /(\?)/gi;
	myString = myString.replace(rExp, " ");
	return myString;
}
function finsesion()
{
	var X = (screen.availWidth - 10) / 4;
	var Y = (screen.availHeight - 45) / 4;
	var Ancho=(screen.availWidth - 10) / 2;
	var Alto=(screen.availHeight - 45) / 2;
	var sPath = "inicio/finsesion.aspx";
	var features = "toolbar=no,status=yes,directories=no,menubar=no,scrollbars=no,top=" + Y + ",left=" + X + ",width=" + Ancho + ",height=" + Alto + '"';
	myWindow = window.open(sPath, "_blank", features);
}
function trimString(str)
{
	while(str.charAt(0) == ' ')
		str = str.substring(1);
	while(str.charAt(str.length - 1) == ' ')
		str = str.substring(0, str.length - 1);
	return str;
}
