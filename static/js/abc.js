window.onload = iniciar;

function iniciar(){
	var lista_botones_arriba = document.querySelectorAll("div div .Arriba")
	var lista_botones_abajo = document.querySelectorAll("div div .Abajo")
	var letras = document.querySelectorAll(".letra")
	var spans = document.querySelectorAll("div span")
	var submit = document.getElementById("submit");
	submit.addEventListener("click",()=>{
		if (checkIsOk(spans) == 1){
			submit.setAttribute("name","submit_bueno")
			
		}
	})
	spans.forEach((nodo,index)=>{		
		lista_botones_arriba.item(index).addEventListener("click",()=>{
			if(index>0){
				temp = spans.item(index-1).innerText
				spans.item(index-1).innerText = nodo.innerText
				nodo.innerText = temp
			}
			else{
				temp = spans.item(spans.length-1).innerText
				spans.item(spans.length-1).innerText = nodo.innerText
				nodo.innerText = temp	
			}
			if (checkIsOk(spans) == 1){
				submit.setAttribute("name","submit_bueno")			
			}
		})
		lista_botones_abajo.item(index).addEventListener("click",()=>{
			if(index<spans.length-1){
				temp = spans.item(index+1).innerText
				spans.item(index+1).innerText = nodo.innerText
				nodo.innerText = temp
			}
			else{
				temp = spans.item(0).innerText
				spans.item(0).innerText = nodo.innerText
				nodo.innerText = temp
			}
			if (checkIsOk(spans) == 1){
				submit.setAttribute("name","submit_bueno")
			}
		})
		

	})
}
function checkIsOk(spans){
	var abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",'Q','R','S','T','U','V','W','X','Y','Z']
	for (var i = 0; i < spans.length-1; i++) {
		if (abc.indexOf(spans.item(i).innerText)>abc.indexOf(spans.item(i+1).innerText)){
			return -1;
		}
	}
	return 1;
}




