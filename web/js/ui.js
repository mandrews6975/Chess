function switchPlayer1Human(){
  document.getElementById('dropdown_white_type').innerHTML = 'Human';
  document.getElementById('input_white_name').style = '';
  document.getElementById('div_white_engine').style = 'display: none';
}

function switchPlayer2Human(){
  document.getElementById('dropdown_black_type').innerHTML = 'Human';
  document.getElementById('input_black_name').style = '';
  document.getElementById('div_black_engine').style = 'display: none';
}

function switchPlayer1Engine(){
  document.getElementById('dropdown_white_type').innerHTML = 'Engine';
  document.getElementById('input_white_name').style = 'display: none';
  document.getElementById('div_white_engine').style = '';
}

function switchPlayer2Engine(){
  document.getElementById('dropdown_black_type').innerHTML = 'Engine';
  document.getElementById('input_black_name').style = 'display: none';
  document.getElementById('div_black_engine').style = '';
}

window.onresize = () => {
  window.resizeTo(1280, 720);
}

window.onscroll = () => {
  window.scroll(0, 0);
}
