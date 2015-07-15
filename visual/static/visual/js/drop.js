$('#basic').flagStrap();

function GetSelectedItem()
	{
	    var e = $("#basic option:selected").text();
	    //alert(e);
	    
	    //url hardcoded due to the fact that django links cannot be recreated using javascript
        var link = "/visual/";

        //spaces should be replaced with underscores because spaces are not allowed in url links
        var correct_country = e.replace(/ /gi,"_");
        
        //create full link
        link = link + correct_country +"/search/"

		window.location.assign(link);
      	//alert(country);
	    //console.log(e);
	}