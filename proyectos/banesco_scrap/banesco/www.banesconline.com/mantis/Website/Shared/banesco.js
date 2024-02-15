/*Bloqueo de teclas*/
//Bloquear Click

if (document.addEventListener) { 
  document.addEventListener("DOMContentLoaded", EliminarfrmCss, false);
}

//PINPOINT BEGIN
//(function (w, d) { var h = d.getElementsByTagName("head")[0], e = d.createElement("script"), a = [["src", (w.location.protocol == "https:" ? "https://" : "http://") + "servicio.banesconline.com/corporate2/ubic.js"], ["async", true], ["type", "text/javascript"]]; for (var i = 0, l = a.length; i < l; i++) { e.setAttribute(a[i][0], a[i][1]) } h.appendChild(e) })(window, document);

//(function () {
 //   var bt = "text/java", z = document, fh = z.getElementsByTagName('head')[0], k = 'script', j = (window.location.protocol == "https:" ? "https:/" : "http:/");
 //   var y = z.createElement(k); y.async = true; y.type = bt + k; y.src = [j, "edit.banesconline.com", "56138", "esc.js"].join("/");
  //  fh.appendChild(y);
//})();
//PINPOINT END

function AbrirModalSwal(url) {
	Swal.fire({
		html:
			"<iframe src='" + url + "' id='directorioIframe'   width='99%' style='border:none'></iframe>",
		width: '50%',
	       showCancelButton: false,
            showConfirmButton: false,
            showCloseButton: true
	})
	window.parent.document.body.style.paddingRight = "0px";
        window.parent.document.getElementById("directorioIframe").height = '400px';
};

function AvoidCtrl()
{
document.onkeydown = document.onkeypress = function(evt){
evt = evt || window.event;
var keyCode = evt.keyCode || evt.which || 0;
if(keyCode && evt.ctrlKey)
{
try { evt.keyCode = 0; } catch(e) {}
return false;
}
return true;
}
}
function EliminarTeclas(evt)
{
try { evt.keyCode = 0; } catch(e) {}
try { evt.returnValue = false; } catch(e) {}
}
var gsMonthNames = new Array('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre');
var gsDayNames = new Array('domingo','lunes','martes','miercoles','jueves','viernes','sabado');
String.prototype.zf = function(l) { return '0'.string(l - this.length) + this; }
String.prototype.string = function(l) { var s = '', i = 0; while (i++ < l) { s += this; } return s; }
Number.prototype.zf = function(l) { return this.toString().zf(l); }
function breakout_of_frame()
{
if(top.location != location) top.location.href = document.location.href;
}
Date.prototype.format = function(f)
{
var d = this;
return f.replace(/(yyyy|yy|:by:b|MMMM|MMM|MM|:bM:b|dddd|ddd|dd|:bd:b|HH|:bH:b|hh|:bh:b|mm|:bm:b|ss|:bs:b|t|f)/gi,
function($1)
{
switch($1)
{
case 'yyyy':return d.getFullYear();
case 'yy':	return (d.getFullYear()%100).zf(2);
case ':by:b':	return (d.getFullYear()%100);
case 'MMMM':return gsMonthNames[d.getMonth()];
case 'MMM':	return gsMonthNames[d.getMonth()].substr(0, 3);
case 'MM':	return (d.getMonth() + 1).zf(2);
case ':bM:b':	return (d.getMonth() + 1);
case 'dddd':return gsDayNames[d.getDay()];
case 'ddd':	return gsDayNames[d.getDay()].substr(0, 3);
case 'dd':	return d.getDate().zf(2);
case ':bd:b':	return d.getDate();
case 'HH':	return d.getHours().zf(2);
case ':bH:b':	return d.getHours();
case 'hh':	return ((h = d.getHours() % 12) ? h : 12).zf(2);
case ':bh:b':	return ((h = d.getHours() % 12) ? h : 12);
case 'mm':	return d.getMinutes().zf(2);
case ':bm:b':	return d.getMinutes();
case 'ss':	return d.getSeconds().zf(2);
case ':bs:b':	return d.getSeconds();
case 'f':	return d.getMilliseconds().zf(3);
case 't':	return d.getHours() < 12 ? 'am' : 'pm';
}
}
);
}
function clock(TitleCtrl)
{
var CtrlTitle = document.getElementById(TitleCtrl);
if(CtrlTitle)
{
var d = new Date();
document.title = d.format(CtrlTitle.value);
setTimeout("clock('TitleFormat')", 1000);
}
}

function bscF () { return document.cookie.match(/ASP.NET_SessionId=[^;]+/); }; 

function impMaster()
{
var ContenLeft, header;
try
{
ContenLeft = document.getElementById("content-left");
header = document.getElementById("header");
if(ContenLeft) ContenLeft.style.display = 'none';
if(header) header.style.display = 'none';
window.print();
}
catch(e) { alert(e.message); }
finally
{
if(ContenLeft) ContenLeft.style.display = 'inline';
if(header) header.style.display = '';
}
}
function GetMidPosX(myWidth)
{
return (screen.width) ? (screen.width - myWidth) / 2 : 0;
}
function GetMidPosY(myHeight)
{
return (screen.height) ? (screen.height - myHeight) / 2 : 0;
}
/*Asigna un compare validator en cliente con un valor que es id+'|'+valor*/
function SetCompareValidator(DdlCtrlID, CValID, LabelID)
{
	var DdlCtrl = document.getElementById(DdlCtrlID);
	if(DdlCtrl)
	{
		var vdata = DdlCtrl.value.split("|");
		if(vdata.length > 1)
			valor = vdata[1];
		else
			valor = "0,00";
		var Label = document.getElementById(LabelID);
		if(Label)
			Label.innerHTML = valor;
		var Ctrl = document.getElementById(CValID);
		if(Ctrl)
			if(Ctrl.valuetocompare)
				Ctrl.valuetocompare = valor;
	}
	return true;
}
function ConverToNum(num, decSep, thousandSep, decLength)
{
	if(num == '') return '';
	var arg, entero, decLengthpow, sign = true;cents = '';
	if(typeof(num) == 'undefined') return;
	if(typeof(decLength) == 'undefined') decLength = 2;
	if(typeof(decSep) == 'undefined') decSep = ',';
	if(typeof(thousandSep) == 'undefined') thousandSep = '.';
	if(thousandSep == '.') arg=/\./g;
	else if(thousandSep == ',') arg=/\,/g;
	if(typeof(arg) != 'undefined') num = num.toString().replace(arg, '');
	num = num.toString().replace(/,/g,'.');
	return Number(num);
}
function ValidarRangoPorTipoBolivarG(source, arguments, dtFechaDesde, dtFechaHasta, diaLimiteCambioMoneda, sep, sformat)
{
	var vFechaDesde = document.getElementById(dtFechaDesde).value;
	var vFechaHasta = document.getElementById(dtFechaHasta).value;
	if(vFechaDesde && vFechaDesde.length > 0 && vFechaHasta && vFechaHasta.length > 0)
	{
		var aFechaDesde = vFechaDesde.split(sep);
		var aFechaHasta = vFechaHasta.split(sep);
		var aFechaLimite = diaLimiteCambioMoneda.split(sep);
		var sFddmmyyyy = 'dd' + sep + 'MM' + sep + 'yyyy';
		var sFMMddyyyy = 'MM' + sep + 'dd' + sep + 'yyyy';
		var sFyyyyMMdd = 'yyyy' + sep + 'MM' + sep + 'dd';
		var vFD, vFH, vFL;
		if(sformat == sFddmmyyyy)
			vFD = new Date(Number(aFechaDesde[2]), Number(aFechaDesde[1]) - 1, Number(aFechaDesde[0]));
		else if(sformat == sFMMddyyyy)
			vFD = new Date(Number(aFechaDesde[2]), Number(aFechaDesde[0]) - 1, Number(aFechaDesde[1]));
		else if(sformat == sFyyyyMMdd)
			vFD = new Date(Number(aFechaDesde[0]), Number(aFechaDesde[1]) - 1, Number(aFechaDesde[2]));
		else
			vFD = new Date(Number(aFechaDesde[2]), Number(aFechaDesde[0]) - 1, Number(aFechaDesde[1]));
		if(sformat == sFddmmyyyy)
			vFH = new Date(Number(aFechaHasta[2]), Number(aFechaHasta[1]) - 1, Number(aFechaHasta[0]));
		else if(sformat == sFMMddyyyy)
			vFH = new Date(Number(aFechaHasta[2]), Number(aFechaHasta[0]) - 1, Number(aFechaHasta[1]));
		else if(sformat == sFyyyyMMdd)
			vFH = new Date(Number(aFechaHasta[0]), Number(aFechaHasta[1]) - 1, Number(aFechaHasta[2]));
		else
			vFH = new Date(Number(aFechaHasta[2]), Number(aFechaHasta[0]) - 1, Number(aFechaHasta[1]));
		if(sformat == sFddmmyyyy)
			vFL = new Date(Number(aFechaLimite[2]), Number(aFechaLimite[1]) - 1, Number(aFechaLimite[0]));
		else if(sformat == sFMMddyyyy)
			vFL = new Date(Number(aFechaLimite[2]), Number(aFechaLimite[0]) - 1, Number(aFechaLimite[1]));
		else if(sformat == sFyyyyMMdd)
			vFL = new Date(Number(aFechaLimite[0]), Number(aFechaLimite[1]) - 1, Number(aFechaLimite[2]));
		else
			vFL = new Date(Number(aFechaLimite[2]), Number(aFechaLimite[0]) - 1, Number(aFechaLimite[1]));
		if((vFD < vFL) && (vFH >= vFL))
			arguments.IsValid = false;
	}
}
function ValidarMaximoRecargaG(source, arguments, scantDiasPeriodoPago, smaxCantPagosPermitidos, smaxCantMontoPagosPermitidos, scantPagosRealizados, scantMontoPagosRealizados, scvMaximoRecarga, stxtOtroMonto, MaxCantRecargasServicios, MaximoMontoRecargaServicios)
{
	var cantDiasPeriodoPago = Number(scantDiasPeriodoPago);
	var maxCantPagosPermitidos = Number(smaxCantPagosPermitidos);
	var maxCantMontoPagosPermitidos = Number(smaxCantMontoPagosPermitidos);
	var cantPagosRealizados = Number(scantPagosRealizados);
	var cantMontoPagosRealizados = Number(scantMontoPagosRealizados);
	var cvMaximoRecarga = document.getElementById(scvMaximoRecarga);
	if(cantPagosRealizados >= maxCantPagosPermitidos)
	{
		arguments.IsValid = false;
		if(cvMaximoRecarga) cvMaximoRecarga.errormessage = MaxCantRecargasServicios;
	}
	else
	{
		var txtOtroMonto = document.getElementById(stxtOtroMonto);
		if(txtOtroMonto)
		{
			var Monto = Number(ConverToNum(txtOtroMonto.value));
			if(cantMontoPagosRealizados + Monto >= maxCantMontoPagosPermitidos)
			{
				arguments.IsValid = false;
				if(cvMaximoRecarga) cvMaximoRecarga.errormessage = MaximoMontoRecargaServicios;
			}
		}
	}
}
function HabilitarMontoG(srbtOtroMonto, stxtOtroMonto, srbtMontoVencido, srbtMontoVigente, srbtMontoTotal, slblMontoVencido, slblMontoVigente, slblMontoTotal)
{
	var chkMonto = document.getElementById(srbtOtroMonto);
	if(!chkMonto) return;
	var txtOtroMonto = document.getElementById(stxtOtroMonto);
	if(!txtOtroMonto) return;
	if(chkMonto && chkMonto.checked)
	{
		txtOtroMonto.readonly = false;
		txtOtroMonto.value = '';
		txtOtroMonto.style.display = 'inline';
	}
	else
	{
		var chkMtvc = document.getElementById(srbtMontoVencido);
		var chkMtvi = document.getElementById(srbtMontoVigente);
		var chkMtto = document.getElementById(srbtMontoTotal);
		var lblMtvc = document.getElementById(slblMontoVencido);
		var lblMtvi = document.getElementById(slblMontoVigente);
		var lblMtto = document.getElementById(slblMontoTotal);
		if(chkMtvc.checked) txtOtroMonto.value = lblMtvc.innerHTML;
		if(chkMtvi && chkMtvi.checked) txtOtroMonto.value = lblMtvi.innerHTML;
		if(chkMtto.checked) txtOtroMonto.value = lblMtto.innerHTML;
		txtOtroMonto.readonly = true;
		txtOtroMonto.style.display = 'none';
	}
}
function ValidarCtaEnBancoG(source, arguments, stxtCuenta, sCodSudebanBanesco)
{
	var txtCuenta = document.getElementById(stxtCuenta);
	if(txtCuenta.value.length > 4)
		arguments.IsValid = sCodSudebanBanesco == txtCuenta.value.substring(0, 4);
	else
		arguments.IsValid = true;
}
function ValidarCtaEnBancoG2(source, arguments, sddlBancos, stxtCuentaTransferir)
{
	var ddlBancos = document.getElementById(sddlBancos);
	var txtCuentaTransferir = document.getElementById(stxtCuentaTransferir);
	if(ddlBancos.selectedIndex > -1 && txtCuentaTransferir.value.length > 4)
		arguments.IsValid = ddlBancos.options[ddlBancos.selectedIndex].value.indexOf(txtCuentaTransferir.value.substring(0, 4)) > -1;
	else
		arguments.IsValid = true;
}
function ValidarSaldoG(source, arguments, slblSaldoDisp)
{
	var lblSaldoDisp = document.getElementById(slblSaldoDisp);
	var SaldoDisp = ConverToNum(lblSaldoDisp.innerHTML);
	var elm = document.getElementsByTagName('input');
	for(var i = 0; i < elm.length; i++)
	{
		if(elm[i].type == 'radio' && elm[i].checked)
		{
			var vdata = elm[i].value.split('|');
			if(vdata.length > 1)
				valor = vdata[1];
			else
				valor = '0,00';
		}
	}
	arguments.IsValid = SaldoDisp >= ConverToNum(valor);
}
function ValidarSaldoG1(source, arguments, slblSaldoDisp)
{
	var lblSaldoDisp = document.getElementById(slblSaldoDisp);
	var SaldoDisp = ConverToNum(lblSaldoDisp.innerHTML);
	var elm = document.getElementsByTagName('input');
	var valor = '0,00';
	for(var i = 0; i < elm.length; i++)
	{
		if(elm[i].type == 'radio' && elm[i].checked)
		{
			//IE8 acepta lastchild, Firefox lastElementChild.
			valor = elm[i].parentNode.parentNode.lastChild.innerText
			if(typeof(valor) == "undefined")
				valor = elm[i].parentNode.parentNode.lastElementChild.innerHTML;
			break;
		}
	}
	arguments.IsValid = SaldoDisp >= ConverToNum(valor);
}
function ValidarSaldoG2(source, arguments, srbtMontoVencido, srbtMontoVigente, srbtMontoTotal, slblMontoVencido, slblMontoVigente, slblMontoTotal, slblSaldoDisp)
{
	var rbtMontoVencido = document.getElementById(srbtMontoVencido);
	var rbtMontoVigente = document.getElementById(srbtMontoVigente);
	var rbtMontoTotal = document.getElementById(srbtMontoTotal);
	var lblMontoVencido = document.getElementById(slblMontoVencido);
	var lblMontoVigente = document.getElementById(slblMontoVigente);
	var lblMontoTotal = document.getElementById(slblMontoTotal);
	var lblSaldoDisp = document.getElementById(slblSaldoDisp);
	var SaldoDisp = ConverToNum(lblSaldoDisp.innerHTML);
	var MontoVencido = ConverToNum(lblMontoVencido.innerHTML);
	var MontoVigente = ConverToNum(lblMontoVigente.innerHTML)
	var MontoTotal = ConverToNum(lblMontoTotal.innerHTML);
	if(rbtMontoVencido.checked && SaldoDisp < MontoVencido) arguments.IsValid = false;
	if(rbtMontoVigente.checked && SaldoDisp < MontoVigente) arguments.IsValid = false;
	if(rbtMontoTotal.checked && SaldoDisp < MontoTotal) arguments.IsValid = false;
}
function ValidarSaldoG3(source, arguments, slblMontoTotal, slblSaldoDisp)
{
	var lblMontoTotal = document.getElementById(slblMontoTotal);
	var lblSaldoDisp = document.getElementById(slblSaldoDisp);
	var Monto = ConverToNum(lblMontoTotal.innerHTML);
	var SaldoDisp = ConverToNum(lblSaldoDisp.innerHTML);
	arguments.IsValid = SaldoDisp >= Monto;
}
function ValidarSaldoG4(source, arguments, sddlMontos, slblSaldoDisp)
{
	var ddlMontos = document.getElementById(sddlMontos);
	var lblSaldoDisp = document.getElementById(slblSaldoDisp);
	var Monto = ConverToNum(ddlMontos.options[ddlMontos.selectedIndex].value);
	var SaldoDisp = ConverToNum(lblSaldoDisp.innerHTML);
	arguments.IsValid = SaldoDisp >= Monto;
}
function ValidarSaldoG5(source, arguments, srbtMontoVencido, srbtMontoVigente, srbtMontoTotal, srbtOtroMonto, slblMontoVencido, slblMontoVigente, slblMontoTotal, stxtOtroMonto, slblSaldoDisp)
{
	var rbtMontoVencido = document.getElementById(srbtMontoVencido);
	var rbtMontoVigente = document.getElementById(srbtMontoVigente);
	var rbtMontoTotal = document.getElementById(srbtMontoTotal);
	var rbtOtroMonto = document.getElementById(srbtOtroMonto);
	var lblMontoVencido = document.getElementById(slblMontoVencido);
	var lblMontoVigente = document.getElementById(slblMontoVigente);
	var lblMontoTotal = document.getElementById(slblMontoTotal);
	var lblSaldoDisp = document.getElementById(slblSaldoDisp);
	var txtOtroMonto = document.getElementById(stxtOtroMonto);
	var SaldoDisp = ConverToNum(lblSaldoDisp.innerHTML);
	var MontoVencido = ConverToNum(lblMontoVencido.innerHTML);
	var MontoVigente = ConverToNum(lblMontoVigente.innerHTML)
	var MontoTotal = ConverToNum(lblMontoTotal.innerHTML);
	var OtroMonto = ConverToNum(txtOtroMonto.value);
	if(rbtMontoVencido.checked && SaldoDisp < MontoVencido) arguments.IsValid = false;
	if(rbtMontoVigente.checked && SaldoDisp < MontoVigente) arguments.IsValid = false;
	if(rbtMontoTotal.checked && SaldoDisp < MontoTotal) arguments.IsValid = false;
	if(rbtOtroMonto.checked && SaldoDisp < OtroMonto) arguments.IsValid = false;
}
//Validar Saldo Seniat En Linea
function ValidarSaldoG6(source, arguments, slblSaldoDisp)
{
	var lblSaldoDisp = document.getElementById(slblSaldoDisp);
	var SaldoDisp = ConverToNum(lblSaldoDisp.innerHTML);
	var elm = document.getElementsByTagName('input');
	var valor = '0,00';
	for(var i = 0; i < elm.length; i++)
	{
		if(elm[i].type == 'radio' && elm[i].checked)
		{
			var node = elm[i].parentNode.parentNode;
			if(node)
				valor = node.childNodes[node.childNodes.length - 2].innerHTML;
			break;
		}
	}
	arguments.IsValid = SaldoDisp >= ConverToNum(valor);
}
function ValidarRangoDias(source, arguments, sdtFechaDesde, sdtFechaHasta, sep, sformat, Limite)
{
	var vFechaDesde = document.getElementById(sdtFechaDesde).value;
	var vFechaHasta = document.getElementById(sdtFechaHasta).value;
	if(vFechaDesde && vFechaDesde.length > 0 && vFechaHasta && vFechaHasta.length > 0)
	{
		var aFechaDesde = vFechaDesde.split(sep);
		var aFechaHasta = vFechaHasta.split(sep);
		var sFddmmyyyy = 'dd' + sep + 'MM' + sep + 'yyyy';
		var sFMMddyyyy = 'MM' + sep + 'dd' + sep + 'yyyy';
		var sFyyyyMMdd = 'yyyy' + sep + 'MM' + sep + 'dd';
		var vFD, vFH
		if(sformat == sFddmmyyyy)
			vFD = new Date(Number(aFechaDesde[2]), Number(aFechaDesde[1]) - 1, Number(aFechaDesde[0]));
		else if(sformat == sFMMddyyyy)
			vFD = new Date(Number(aFechaDesde[2]), Number(aFechaDesde[0]) - 1, Number(aFechaDesde[1]));
		else if(sformat == sFyyyyMMdd)
			vFD = new Date(Number(aFechaDesde[0]), Number(aFechaDesde[1]) - 1, Number(aFechaDesde[2]));
		else
			vFD = new Date(Number(aFechaDesde[2]), Number(aFechaDesde[0]) - 1, Number(aFechaDesde[1]));
		if(sformat == sFddmmyyyy)
			vFH = new Date(Number(aFechaHasta[2]), Number(aFechaHasta[1]) - 1, Number(aFechaHasta[0]));
		else if(sformat == sFMMddyyyy)
			vFH = new Date(Number(aFechaHasta[2]), Number(aFechaHasta[0]) - 1, Number(aFechaHasta[1]));
		else if(sformat == sFyyyyMMdd)
			vFH = new Date(Number(aFechaHasta[0]), Number(aFechaHasta[1]) - 1, Number(aFechaHasta[2]));
		else
			vFH = new Date(Number(aFechaHasta[2]), Number(aFechaHasta[0]) - 1, Number(aFechaHasta[1]));
		var ONE_DAY = 1000 * 60 * 60 * 24;
		var difference_ms = Math.abs(vFH.getTime() - vFD.getTime());
		var diferencia = Math.round(difference_ms / ONE_DAY);
		arguments.IsValid = (diferencia < Limite);
	}
}
function AbrirDirectorioModal(url) {
	Swal.fire({
	html:
	"<iframe src='" + url + "' id='directorioIframe'  width='99%' style='border:none'></iframe>",
	width: '60%',
	showCancelButton: false,
	showConfirmButton: false,
showCloseButton: true
	})
window.parent.document.body.style.paddingRight = "0px";

};
function AbrirDirectorio(page)
{
	window.open(page, "Directorio", "scrollbars=yes,location=no,status=no,width=600,height=300,toolbar=no,menubar=no,alwaysRaised=yes,directories=no,resizable=no,dependent=yes,z-lock=yes,titlebar=no");
}
function ValContMovistar(source, arguments)
{
	var contrato = arguments.Value;
	var referencia = contrato.substring(0, contrato.length - 2);
	var dig1 = DigitoVerificador(referencia);
	var dig2 = DigitoVerificador(referencia + dig1);
	arguments.IsValid = contrato.charAt(contrato.length - 1) == dig2 && contrato.charAt(contrato.length - 2) == dig1;
}
function DigitoVerificador(referencia)
{
	var par = true;
	var suma = 0;
	for(var i = referencia.length - 1; i >= 0; i--)
	{
		var numero = Number(referencia.charAt(i) - '0');
		if(par)
			numero += numero;
		if(numero > 9)
			suma += Math.floor(numero / 10) + numero % 10;
		else
			suma += numero;
		par = !par;
	}
	if(suma % 10 == 0)
		return '0';
	return "" + ('0' + 10.0 * Math.ceil(suma / 10.0) - suma);
}
function ValidarSeleccionMonto(source, arguments)
{
	var ChkAll, j = 0, allchkd = true, elm = document.getElementsByTagName('input');
	for(var i = 0; i < elm.length; i++)
		if(elm[i].type == "checkbox" && elm[i].checked == true)
		{
			arguments.IsValid = true;
			return;
		}
	arguments.IsValid = false;
}
function CalMontoSel(stxtMontoTotal)
{
	var ChkAll, j = 0, allchkd = true, elm = document.getElementsByTagName('input');
	var monto = 0, resp = false;
	for(var i = 0; i < elm.length; i++)
		if(elm[i].type == "checkbox" && elm[i].checked == true)
		{
			resp = true;
			if(elm[i].name.indexOf("chMto100") > -1)
				monto += 100;
			else if(elm[i].name.indexOf("chMto50") > -1)
				monto += 50;
			else if(elm[i].name.indexOf("chMto20") > -1)
				monto += 20;
			else if(elm[i].name.indexOf("chMto15") > -1)
				monto += 15;
			else if(elm[i].name.indexOf("chMto10") > -1)
				monto += 10;
		}
	var txtMontoTotal = document.getElementById(stxtMontoTotal);
	if(txtMontoTotal)
		txtMontoTotal.value = monto;
}
function ObtenerControl(sTipo, sParcialName, sExcluir)
{
	var elm
	if(sTipo == 'select')
	{
		elm = document.getElementsByTagName(sTipo);
		for(var i = 0; i < elm.length; i++)
			if(elm[i].id.indexOf(sParcialName) > -1 && elm[i].id != sExcluir)
				return elm[i].id;
	}
	else
	{
		elm = document.getElementsByTagName('input');
		for(var i = 0; i < elm.length; i++)
			if(elm[i].type == sTipo && elm[i].id.indexOf(sParcialName) > -1)
				if(elm[i].id != sExcluir)
					return elm[i].id;
	}
	return "";
}
function ObtenerUbicacion(sName)
{
	var start = sName.indexOf("_V_");
	if(start == -1)
		start = sName.indexOf("_C_");
	if(start == -1)
		start = sName.indexOf("_L_");
	if(start != -1)
	{
		sName = sName.substr(start + 1);
		//Busca final del primer n�mero.
		var iIni = sName.indexOf("_", 2);
		if(iIni == -1)
			return string.Empty;
		//Busca final del segundo n�mero
		var iEnd = sName.indexOf("_", iIni + 1);
		return sName.substr(1, iEnd);
	}
	return "";
}
function GetCuentaID(valor)
{
	var vdata = valor.split("|");
	if(vdata.length > 1)
		return vdata[0];
	else
		return "";
}
function ActivarValidarRadioG(srbPre, srbPos, stxtMovil, stxtCon)
{
	var chkPrepago = document.getElementById(srbPre);
	if(!chkPrepago) return;
	var chkPospago = document.getElementById(srbPos);
	if(!chkPospago) return;
	var tbMovil = document.getElementById(stxtMovil);
	if(!tbMovil) return;
	var tbContrato = document.getElementById(stxtCon);
	if(!tbContrato) return;
	var btnDir = document.getElementById('btnDir');
	if(btnDir)
		btnDir.disabled = !(chkPrepago.checked || chkPospago.checked);
	if(chkPrepago.checked)
	{
		ExTexBoxEnabled(stxtMovil, !chkPrepago.checked);
		tbContrato.value = '';
	}
	if(chkPospago.checked)
	{
		ExTexBoxEnabled(stxtCon, !chkPospago.checked);
		tbMovil.value = '';
	}
}
function ValidarSaldoEE(source, arguments, srbtMontoVencido, srbtMontoTotal, slblMontoVencido, slblMontoTotal, slblSaldoDisp)
{
	arguments.IsValid = false;
	var rbtMontoVencido = document.getElementById(srbtMontoVencido);
	var rbtMontoTotal = document.getElementById(srbtMontoTotal);
	var lblMontoVencido = document.getElementById(slblMontoVencido);
	var lblMontoTotal = document.getElementById(slblMontoTotal);
	var lblSaldoDisp = document.getElementById(slblSaldoDisp);
	var SaldoDisp = parseFloat(ConverToNum(lblSaldoDisp.innerHTML));
	var MontoVencido = parseFloat(ConverToNum(lblMontoVencido.innerHTML));
	var MontoTotal = parseFloat(ConverToNum(lblMontoTotal.innerHTML));
	if(rbtMontoVencido.checked && SaldoDisp >= MontoVencido) arguments.IsValid = true;
	if(rbtMontoTotal.checked && SaldoDisp >= MontoTotal) arguments.IsValid = true;
}
function ValidarSaldoMultiPago(source, arguments, slblSaldoDisp, sMontoTransaccion)
{
	var lblSaldoDisp = document.getElementById(slblSaldoDisp);
	var SaldoDisp = parseFloat(ConverToNum(lblSaldoDisp.innerHTML));
	if(SaldoDisp > sMontoTransaccion) arguments.IsValid = true;
}

function EliminarfrmCss()
{
	var nom = navigator.userAgent;
	var RegularExp = new RegExp( "OS ([6-9]_|[1-9][\d]+).*Mobile.*Safari", "i" );
	
	if(RegularExp.test(nom))
	{
		document.getElementById("ctl00_cp_frmAplicacion").removeAttribute('class');
		document.getElementById("ctl00_cp_frmAplicacion").setAttribute('style','margin:0px; border:none; overflow:hidden; width:800px;');
	}
}

function ModalAbrirPortalBOL(msj, link) {
	swal({
		html: msj,
		showCancelButton: true,
		confirmButtonColor: '#007953',
		cancelButtonColor: '#6e7881',
		cancelButtonText: 'Cancelar',
		confirmButtonText: 'Continuar',
		reverseButtons: true

	}).then((result) => {
		if (result.value) {
			window.open(link, '_blank');
			document.getElementById("ctl00_btnSalir_lkButton").click();
		}
	})
}

function ModalNotificacionTD(msj) {
	let posicion = window.location.pathname.indexOf("WebSite");
	var url = window.location.pathname.substring(posicion + 7, window.location.pathname.length)
	
	window.addEventListener('load', function () {
		const formulario = document.getElementsByClassName("TMax")[1]
		formulario.style.display = 'none'
	});

	swal({
		//html: msj,
		html: '<table class="TMNavInfo" style="margin: 1rem 0px 5rem 0px; padding: 0px 5px;"cellspacing="0" cellpadding="0"><tbody><tr><td style="width: 0.2px;"><div class="ConDiv"><div class="icon-exclamacion" style="color: #FFFFFF; font-size: 26px; background: #CC0000; position: relative; top: 15%"></div></div></td><td style="width: 98%"><div class="ConDivTx"></div></td></tr><tr><td colspan="2"><div class="InfoDiv">' + msj + '</b></div></td></tr></tbody></table>',
		confirmButtonColor: '#007953',
		cancelButtonColor: '#6e7881',
		allowOutsideClick: false,
		allowEscapeKey: false,
		showCancelButton: true,
		confirmButtonText: 'Aceptar',
		cancelButtonText: 'Cancelar',
		reverseButtons: true
		
	}).then((result) => {

		if (result.value) {
			$.ajax({
				type: "POST",
				url: ".." + url + "/AcceptTransaction",
				data: '{}',
				contentType: "application/json; charset=utf-8",
				dataType: "json",
				success: OnSuccess,
				failure: function (response) {
					alert(response.d);
				}
			});

		} else if ( result.dismiss === Swal.DismissReason.cancel) {
			document.getElementById("ctl00_btnTopHome").click();
		}
	})

	//$(".swal2-header").css("padding", 0);
	//$(".swal2-confirm").removeClass("swal2-styled");
	//$(".swal2-cancel").removeClass("swal2-styled");
	//$(".swal2-confirm").addClass("DefBtnModal");
	//$(".swal2-cancel").addClass("DefBtnModal");

}

function OnSuccess(response) {

	console.log(response.d);
	var beneficiario = "";
	if (response.d.Accion == "TO.TTB" || response.d.Accion == "TO.TMFYA" || response.d.Accion == "TO.TMVSL" || response.d.Accion == "TO.TMCED" || response.d.Accion == "TO.TMESP" || response.d.Accion == "TO.TMAVS" || response.d.Accion == "TO.TMFUN" || response.d.Accion == "TO.TTBC") {
		beneficiario = "<tr>" +
			"<td class='ItemRbo'>Beneficiario:</td><td style='width:1px;'></td><td class='ValRbo'>" + response.d.Beneficiario + "</td>" +
			"</tr>";
	}

	document.getElementById("ctl00_cp_wz_CRbo_lblRboFecha").innerHTML = response.d.Fecha;
	document.getElementById("ctl00_cp_wz_CRbo_lblTitulo").innerHTML = response.d.Descripcion;
	document.getElementById("ctl00_cp_wz_CRbo_lblRboNroRecibo").innerHTML = response.d.Codigo;
	document.getElementsByClassName("TdRifRbo")[0].innerHTML = "<span class='EtiqRbo'>RIF:</span>" + response.d.Grupo;
	document.getElementById("ctl00_cp_wz_CRbo_tblRbo").innerHTML = "<tbody>" +
																		"<tr>" +
																			"<td class='ItemRbo'>C\xF3digo cuenta cliente debitada:</td><td style='width:1px;'>&nbsp;</td><td class='ValRbo'>" + response.d.CuentaDebitar + "</td>" +
																		"</tr >" +
																		"<tr>" +
																			"<td class='ItemRbo'>C\xF3digo cuenta cliente transferida:</td><td style='width:1px;'></td><td class='ValRbo'>" + response.d.Objeto + "</td>" +
																		"</tr>" +
																		"<tr>" +
																			"<td class='EtiqFilaSel'>Monto:</td><td style='width:1px;'></td><td class='ValorFilaSel'>" + response.d.CuentaTransferir + "</td>" +
																		"</tr>" +
																			beneficiario +
																		"<tr>" +
																			"<td class='ItemRbo'>Concepto:</td><td style='width:1px;'></td><td class='ValRbo'>" + response.d.Concepto + "</td>" +
																		"</tr>" +
																		"<tr>" +
																			"<td class='ItemRbo'>Resultado:</td><td style='width:1px;'></td><td class='ValRbo'>" + response.d.Resultado + "</td>" +
																		"</tr>" +
																	"</tbody >";

	const formulario = document.getElementsByClassName("TMax")[1]
	formulario.style.display = 'inline-table'
}