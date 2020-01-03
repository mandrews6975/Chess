function startNewGame(){
  let whiteType, blackType, whiteID, blackID;
  if(document.getElementById('input_white_name').style.display == ''){
    whiteType = 'human';
    whiteID = document.getElementById('input_white_name').value;
  }else{
    whiteType = 'engine';
    whiteID = document.getElementById('input_white_engine').value;
  }
  if(document.getElementById('input_black_name').style.display == ''){
    blackType = 'human';
    blackID = document.getElementById('input_black_name').value;
  }else{
    blackType = 'engine';
    blackID = document.getElementById('input_black_engine').value;
    console.log(blackID);
  }
  eel.startNewGame(whiteType, blackType, whiteID, blackID)(() => {
    document.getElementById('board_display').style.display = 'block';
  });
}

async function selectWhiteEngine(){
  let path = await eel.selectFile()();
  document.getElementById('input_white_engine').value = path;
}

async function selectBlackEngine(){
  let path = await eel.selectFile()();
  document.getElementById('input_black_engine').value = path;
}

eel.expose(updateBoardDisplay);
function updateBoardDisplay(url){
  document.getElementById('board_display').src = url;
}

eel.expose(openMoveInput);
function openMoveInput(curMove){
  document.getElementById('move_color').innerHTML = curMove.charAt(0).toUpperCase() + curMove.substring(1);
  document.getElementById('input_move').readOnly = false;
  document.getElementById('button_next_move').readOnly = false;
}

eel.expose(closeMoveInput);
function closeMoveInput(curMove){
  document.getElementById('move_color').innerHTML = curMove.charAt(0).toUpperCase() + curMove.substring(1);
  document.getElementById('input_move').readOnly = true;
  document.getElementById('button_next_move').readOnly = true;
}

async function nextMove(){
  let move = document.getElementById('input_move').value;
  let legal = await eel.testMove(move)();
  if(legal){
    eel.submitMove(move);
    document.getElementById('input_move').value = ''
  }else{
    document.getElementById('input_move').value = 'INV';
  }
  document.getElementById('input_move').focus();
}

eel.expose(updatePgnDisplay)
function updatePgnDisplay(pgn){
  document.getElementById('pgn_display').innerHTML = pgn;
}

eel.expose(endGame);
function endGame(method){

}
