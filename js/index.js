function openLoginOption(){
	$(".overlay").show();
	$('#loginPage').addClass("md-show");
	$('#loginEmail').focus();
}

function hideLoginPage(){
	$("#loginErrorMsg").html("");
	$('#loginPage').removeClass("md-show");
	$('.overlay').css("display","none");
}

function loginUser1(){
	var xmlhttp = new XMLHttpRequest();
		var email = document.getElementById("email").value;
		var password = document.getElementById("password").value;
		
		if(email.length>0 && password.length>0){
			if(email=="test@gmail.com" && password=="test"){
				hideLoginPage();
				$("#welcomeMsg").html("Sarah Watson");
				$("#welcomeMsg").show();
				$("#userPic").attr("src", "images/sarah.png");
				$("#userPic").attr("width", "50px");
				$("#userPic").attr("height", "50px");
				$("#loginBtn").hide();
				$("#registerBtn").hide();
			}
		}
		else{
			hideLoginPage();
		}
}

var email;

function loginUser() {	  
		email = document.getElementById("email").value;
		var password = document.getElementById("password").value;
		
		if(email.length>0 && password.length>0){
			  	if(email=="johnson.d@gmail.com" && password=="dave"){
					hideLoginPage();
					$("#welcomeMsg").html("Hey, Dave Johnson!");
					$("#welcomeMsg").show();
					$("#userPic").attr("src", "images/dave.jpg");
					$("#userPic").attr("width", "50px");
					$("#userPic").attr("height", "50px");
					$("#loginBtn").hide();
					$("#registerBtn").hide();
				}
				else{
					hideLoginPage();
				}
			}
		else{
			hideLoginPage();
		}
	}

function submitUserSearch(){
	if(email!=null && email!=undefined && email.length>0){
		var location = $("#placeField").val();
		var from = $("#from").val();
		var till = $("#till").val();
			
			if(location.length>0 && from.length>0 && till.length>0){
				$.session.set("location", location);
				$.session.set("from", from);
				$.session.set("till", till);
				window.location.href='results.html?location='+location + '&from=' + from + '&till=' + till;	

			}
			else{
				hideLoginPage();
			}
		}
}

function buyTour(){
	alert("hey");
	$(this).attr('color', '#f0b740');
}
