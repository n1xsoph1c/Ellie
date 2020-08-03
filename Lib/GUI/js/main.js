async function send_msg(){
	let input = document.getElementById('input').value;
	let output = await eel.get_reply_from_ellie(input)();
	let output_div = document.getElementById('inbox');

	output_div.innerHTML = output;
}

eel.expose(btn_switch);
function btn_switch(a, b, c, d) {
  if (a == true){
	document.getElementById("TTS").innerHTML = "Turn off";
	document.getElementById("TTS").value = "Turn off";
  }else{
	document.getElementById("TTS").innerHTML = "Turn on";
	document.getElementById("TTS").value = "Turn on";
  }on

  if (b == true){
	document.getElementById("onM").innerHTML = "Turn off";
	document.getElementById("onM").value = "Turn off";
  }else{
	document.getElementById("onM").innerHTML = "Turn on";
	document.getElementById("onM").value = "Turn on";
  }

  if (c == true){
	document.getElementById("ofM").innerHTML = "Turn off";
	document.getElementById("ofM").value = "Turn off";
  }else{
	document.getElementById("ofM").innerHTML = "Turn on";
	document.getElementById("ofM").value = "Turn on";
  }

  if (d == true){
	document.getElementById("dM").innerHTML = "Turn off";
	document.getElementById("dM").value = "Turn off";
  }else{
	document.getElementById("dM").innerHTML = "Turn on";
	document.getElementById("dM").value = "Turn on";
  }
}