function switchPlayer1Human(){
  document.getElementById('dropdown_player_1_type').innerHTML = 'Human';
  document.getElementById('input_player_1_name').style = '';
  document.getElementById('div_player_1_engine').style = 'display: none';
}

function switchPlayer2Human(){
  document.getElementById('dropdown_player_2_type').innerHTML = 'Human';
  document.getElementById('input_player_2_name').style = '';
  document.getElementById('div_player_2_engine').style = 'display: none';
}

function switchPlayer1Engine(){
  document.getElementById('dropdown_player_1_type').innerHTML = 'Engine';
  document.getElementById('input_player_1_name').style = 'display: none';
  document.getElementById('div_player_1_engine').style = '';
}

function switchPlayer2Engine(){
  document.getElementById('dropdown_player_2_type').innerHTML = 'Engine';
  document.getElementById('input_player_2_name').style = 'display: none';
  document.getElementById('div_player_2_engine').style = '';
}

window.onresize = () => {
  window.resizeTo(1280, 720);
}
