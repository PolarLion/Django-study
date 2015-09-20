$(function() {
	$("#translate").on("click", function() {
		// debugger;
/*		if ("disabled" == $(this).attr("disabled")) {
			return;
		}
		$(this).attr("disabled", "disabled");*/
		var var1=document.getElementById("sourceinput").value;
		$("#targetinput").html(decodeURI(var1));
	});

});

