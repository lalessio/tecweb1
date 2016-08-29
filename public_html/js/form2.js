
function orario_check(){


	if (document.getElementById("errore_orario") !== "") {
	    document.getElementById("errore_orario").innerHTML = "";
		}


        var hour=document.getElementById("new_hour").value;
        
        if (!hour.replace(/^\s+/g, '').length)
        {
           document.getElementById("errore_orario").innerHTML = "il campo orario è obbligatorio*";
           document.getElementById("new_hour").focus();
           return false;
	}
	else 


	//Finiti i controlli do l'ok
                return true;
		
}
