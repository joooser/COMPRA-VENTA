function doSnoop() {
     
 try {
 var resultado=window.navigator.appName;
 resultado += "|" + window.navigator.appVersion;

 resultado +="|" + window.navigator.platform;

 resultado +="|"+ window.navigator.userAgent;

  resultado += "|" + window.screen.height;

 resultado += "|" + window.screen.width;

 resultado += "|" + window.screen.colorDepth;

 resultado += "|" + window.screen.availWidth;

 resultado += "|" + window.screen.availHeight;
  
  return resultado;
 }
 catch (e) {
 }

}
try {
		var huella =  document.getElementById('huella');
		huella.value=doSnoop();
		
		} catch(err) {}
