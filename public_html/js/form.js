
function price_check(){



	if (document.getElementById("errore_prezzo2") !== "") {
	    document.getElementById("errore_prezzo2").innerHTML = "";
		}



	var price = document.getElementById("new_price").value;	
        
        if (!price.replace(/^\s+/g, '').length)
        {
           document.getElementById("errore_prezzo2").innerHTML = "il campo prezzo è obbligatorio*";
           document.getElementById("new_price").focus();
           return false;
	}
	else 

	//Finiti i controlli do l'ok
                return true;
		
}
