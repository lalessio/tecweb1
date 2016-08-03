
function price_check(){


	if (document.getElementById("errore_prezzo1") !== "") {
	    document.getElementById("errore_prezzo1").innerHTML = "";
		}

	if (document.getElementById("errore_prezzo2") !== "") {
	    document.getElementById("errore_prezzo2").innerHTML = "";
		}



	var pricePA = document.getElementById("new_pricePA").value;	
        var priceE=document.getElementById("new_priceE").value;
        
        if (!pricePA.replace(/^\s+/g, '').length)
        {
           document.getElementById("errore_prezzo1").innerHTML = "il campo prezzo primavera/autunno è obligatorio*";
           document.getElementById("new_pricePA").focus();
           return false;
	}
	else 
		if( !priceE.replace(/^\s+/g, '').length){

			document.getElementById("errore_prezzo2").innerHTML = "il campo prezzo estate è obligatorio*";
			document.getElementById("new_priceE").focus();
           return false;
		}
		else

	//Finiti i controlli do l'ok
                return true;
		
}
