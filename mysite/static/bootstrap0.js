$(function() {
	$("#nmt").on("click", function() {
		// debugger;
/*		if ("disabled" == $(this).attr("disabled")) {
			return;
		}
		$(this).attr("disabled", "disabled");*/
		var var1=document.getElementById("sourceinput").value;
		$("#targetinput").html(decodeURI(var1));
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

