var contact_main_page="\
  <div class=\"row\">\
    <div class=\"col-md-6\"><h3><p class=\"text-center\"><strong>Contact</h3></div>\
    <div class=\"col-md-6\"><h3><p class=\"text-center\"><strong>Source</h3></div>\
  </div>\
  <div class=\"row\">\
    <div class=\"col-md-6\">\
      <h4><p class=\"text-center\">E-mail: <a href=\"mailto:#\" target=\"_blank\">eric900404@gmail.com</a></p></h4>\
      <h4><p class=\"text-center\">Room 1008, Center Building,<br>Beijing Institute of Technology, No. 5 South Zhong Guan Cun Street,<br>Haidian Beijing 100081, P.R. China\
      </p></h4>\
      <h4><p class=\"text-center\">School of Computer Science, <a href\"http://english.bit.edu.cn/\" target=\"_blank\">Beijing Institute of Technology</a>\
    </div>\
    <div class=\"col-md-6\">\
      <h4><p class=\"text-center\">website source: <a href=\"https://github.com/PolarLion/Django-study\" target=\"_blank\">https://github.com/PolarLion/Django-study</a></p></h4>\
      <h4><p class=\"text-center\">nmt source: <a href=\"https://github.com/lisa-groundhog/GroundHog\" target=\"_blank\">https://github.com/lisa-groundhog/GroundHog</a></p></h4>\
      <h4><p class=\"text-center\">smt source: <a href=\"http://www.statmt.org/moses/\" target=\"_blank\">http://www.statmt.org/moses/</a></p></h4>\
    </div>\
  </div>\
" 
$(function() {
	$("#nmt").on("click", function() {
		//debugger;
		var xmlhttp;
		if (window.XMLHttpRequest) {
		    // code for IE7+, Firefox, Chrome, Opera, Safari
		    xmlhttp=new XMLHttpRequest();
		  } else {
		    // code for IE6, IE5
		    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		var var1=document.getElementById("sourceinput").value;
    if (var1 ==''){
      //alert('null input');
      document.getElementById("sourceinput").focus();
    }
    else {
		xmlhttp.open("GET", "/polarlion/nmt/" + var1 , true);
		xmlhttp.setRequestHeader("X-Requested-With", "XMLHttpRequest");
		xmlhttp.send();
		xmlhttp.onreadystatechange=function() {
		  if (xmlhttp.readyState==4 && xmlhttp.status==200) {
		  	// $('#targetinput').html(decodeURI(ret))
		      document.getElementById("targetinput").innerHTML=xmlhttp.responseText;
		  }
		}
    }
	});
	$("#smt").on("click", function() {
    //var var1=document.getElementById("sourceinput").value;
		$("#targetinput").html(decodeURI("undefined operation"));
	});
	$("#save-result").on("click", function() {
		$("#targetinput").html(decodeURI("undefined operation"));
	});
  $("#nav-home").on("click", function(){
    document.getElementById("nav-contact").className=""
    document.getElementById("nav-home").className="active"
    document.getElementById("main-page").innerHTML="\
        <div class=\"row\">\
          <div class=\"col-md-4 col-md-offset-1\"><h3><strong><p class=\"text-left\">Chinese-English Translate</p></strong></h3></div>\
        </div>\
        <div class=\"row\">\
          <div class=\"col-md-5 col-md-offset-1\">\
            <textarea class=\"form-control\" id=\"sourceinput\" placeholder=\"Chinese\" rows=\"6\"></textarea>\
          </div>\
          <div class=\"col-md-5 col-md-offset-0\">\
            <textarea class=\"form-control\" id=\"targetinput\" placeholder=\"English\" rows=\"6\" readonly></textarea>\
          </div>\
        </div>\
        <div class=\"row\">\
          <div class=\"col-md-2 col-md-offset-1\"><h3><a id=\"nmt\" class=\"button button-raised button-inverse button-block\">NMT</a></h3></div>\
          <div class=\"col-md-2 col-md-offset-0\"><h3><a id=\"smt\" class=\"button button-raised button-inverse button-block\">SMT</a></h3></div>\
          <div class=\"col-md-2 col-md-offset-4\"><h3><a id=\"save-result\" class=\"button button-raised button-inverse button-block\">Save Result</a></a></h3></div>\
        </div>\
    "
  });
  $("#nav-contact").on("click", function(){
    //debugger;
    document.getElementById("nav-contact").className="active"
    document.getElementById("nav-home").className=""
    document.getElementById("main-page").innerHTML=contact_main_page
  });
  $("#footer-contact").on("click", function(){
    //debugger;
    document.getElementById("nav-contact").className="active"
    document.getElementById("nav-home").className=""
    document.getElementById("main-page").innerHTML=contact_main_page
  });
});
window.onload=function(){
  //debugger
  //document.getElementById("rain").innerHTML = "hehehehheeheheheh";
  //document.getElementById("time").innerHTML = "2333";
  var tbl=document.createElement('table');
  var tb2=document.createElement('table');
  //tb1.style.color="#ff0040";
  //body=document.body;
  //body.style.backgroundColor='#FFF';
  //body.style.color='#000';
  //body.style.fontFamily='Lucida Console';
  for(var i = 0; i <= 6; i++){
    var tr1 = tbl.insertRow();
    var tr2 = tb2.insertRow();
    for(var j = 0; j <= 15; j++){
      var td1= tr1.insertCell();
      var td2= tr2.insertCell();
      td1.style.width="2%";
      td2.style.width="2%";
    }
  }
  document.getElementById("rain1").appendChild(tbl);
  document.getElementById("rain2").appendChild(tb2);
  setInterval(function(){
    rain(Math.floor((Math.random()*15)),0)
  },20);
  //document.getElementById("rain1").innerHTML = tb1;
}

function rain(n,i) {          
  setTimeout(function (){
    var e=document.getElementsByTagName('tr')[i].childNodes[n];
    e.style.color='#f2f2f2';
    if (i < 7) e.innerHTML = '&#'+Math.floor((Math.random()*200)+0x4E00)+';';
    else e.innerHTML = '&#'+Math.floor((Math.random()*127)+64)+';';
    setTimeout(function(){e.style.color='#bdbdbd'},1000)
    if (i++ < 13) rain(n,i);
  },20);
};

function timeFormat(){
  //debugger
  var today = new Date();
  year = today.getFullYear(),
  month = today.getMonth() + 1,
  day = today.getDate(),
  hour = today.getHours(),
  minute = today.getMinutes(),
  second = today.getSeconds(),
  week = today.getDay(),
  //weekend = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"],
  weekend = ["Sunday","Monday","Tuesday","Wednesday","Thurday","Friday","Saturday"],
  weekDay = weekend[week];
  month < 10 ? month = "0" + month:month;
  day < 10 ? day = "0" + day:day;
  hour < 10 ? hour = "0" + hour:hour;
  minute < 10 ? minute = "0" + minute:minute;
  second < 10 ? second = "0" + second:second;
  var time = year+"-"+month+"-"+day+" "+hour+":"+minute+":"+second + " "+weekDay;
  //var time = year+"-"+month+"-"+day+" "+weekDay;
  document.getElementById("time").innerHTML = time;
}

setInterval(timeFormat,0);
//setInterval(matrix,1);
