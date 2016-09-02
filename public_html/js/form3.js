
function notizia_check(){


	if (document.getElementById("errore_notizia1") !== "") {
	    document.getElementById("errore_notizia1").innerHTML = "";
		}
		if (document.getElementById("errore_notizia2") !== "") {
	    document.getElementById("errore_notizia2").innerHTML = "";
		}


        var title=document.getElementById("new_title").value;
         var content=document.getElementById("new_content").value;
        
        if (!title.replace(/^\s+/g, '').length)
        {
           document.getElementById("errore_notizia1").innerHTML = "il campo title è obligatorio*";
           document.getElementById("new_title").focus();
           return false;
	}
	else if (!content.replace(/^\s+/g, '').length)
        {
           document.getElementById("errore_notizia2").innerHTML = "il campo testo è obligatorio*";
           document.getElementById("new_content").focus();
           return false;
	}


	//Finiti i controlli do l'ok
                return true;
		
}
