$('#basic').flagStrap();

function GetSelectedItem()
	{
	    var e = $("#basic option:selected").text();
	    //alert(e);
	    var a = document.createElement('a');
        var linkText = document.createTextNode("Click here to contine");
        a.appendChild(linkText);
        a.title = "continue";
        a.href = "http://127.0.0.1:8000/visual/country/";
        document.body.appendChild(a);
      	//alert(country);
	    //console.log(e);
	}