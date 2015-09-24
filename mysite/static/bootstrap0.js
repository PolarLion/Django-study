$(function() {
	$("#nmt").on("click", function() {
		// debugger;
/*		if ("disabled" == $(this).attr("disabled")) {
			return;
		}
		$(this).attr("disabled", "disabled");*/
		var xmlhttp;
		if (window.XMLHttpRequest) {
		    // code for IE7+, Firefox, Chrome, Opera, Safari
		    xmlhttp=new XMLHttpRequest();
		  } else {
		    // code for IE6, IE5
		    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		var var1=document.getElementById("sourceinput").value;
		xmlhttp.open("GET", "/nmt/" + var1, true);
		xmlhttp.setRequestHeader("X-Requested-With", "XMLHttpRequest");
		xmlhttp.send();
        // $.ajax("/nmt/",{'a':var1}, function(ret){
        //     $('#targetinput').html(decodeURI(ret))
        // })
		xmlhttp.onreadystatechange=function() {
		  if (xmlhttp.readyState==4 && xmlhttp.status==200) {
		  	// $('#targetinput').html(decodeURI(ret))
		      document.getElementById("targetinput").innerHTML=xmlhttp.responseText;
		  }
		}
	});
	$("#smt").on("click", function() {
		// debugger;
/*		if ("disabled" == $(this).attr("disabled")) {
			return;
		}
		$(this).attr("disabled", "disabled");*/
		var var1=document.getElementById("sourceinput").value;
		$("#targetinput").html(decodeURI(var1));
	});
	$("#save-result").on("click", function() {
		// debugger;
/*		if ("disabled" == $(this).attr("disabled")) {
			return;
		}
		$(this).attr("disabled", "disabled");*/
		// var var1=document.getElementById("sourceinput").value;
		$("#targetinput").html(decodeURI("sssssss"));
	});
});

