import eel, platform, sys, datetime, urllib.request, urllib.parse, chess, chess.pgn, chess.engine
from tkinter import Tk
from tkinter.filedialog import askopenfilename

eel.init("web")

whiteType = None
blackType = None
whiteID = None
blackID = None
curMove = None
curMoveNum = None
board = None
pgn = None
node = None
engine = chess.engine.SimpleEngine.popen_uci("C:\\Users\\Michael\\Documents\\stockfish\\Windows\\stockfish_10_x64.exe")
engineTime = 1.0
whiteEngine = None
blackEngine = None

@eel.expose
def startNewGame(wType, bType, wID, bID):
    global whiteType
    whiteType = wType
    global blackType
    blackType = bType
    global whiteID
    whiteID = wID
    global blackID
    blackID = bID
    global curMove
    curMove = "white"
    global curMoveNum
    curMoveNum = 1
    global board
    board = chess.Board()
    global pgn
    pgn = chess.pgn.Game()
    pgn.headers["Event"] = "Desktop Chess"
    pgn.headers["Site"] = platform.node()
    pgn.headers["Date"] = datetime.datetime.now()
    pgn.headers["Round"] = "1"
    pgn.headers["White"] = whiteID
    pgn.headers["Black"] = blackID
    eel.updatePgnDisplay(str(pgn))
    updateBoardDisplay()
    if whiteType == "engine":
        global whiteEngine
        whiteEngine = chess.engine.SimpleEngine.popen_uci(whiteID)
    if blackType == "engine":
        global blackEngine
        blackEngine = chess.engine.SimpleEngine.popen_uci(blackID)
    if whiteType == "human":
        eel.openMoveInput(curMove)
    else:
        makeEngineMove(whiteEngine)

@eel.expose
def selectFile():
    Tk().withdraw()
    return askopenfilename()

@eel.expose
def testMove(move):
    global board
    return chess.Move.from_uci(move) in board.legal_moves

@eel.expose
def submitMove(move):
    global board
    global curMove
    global pgn
    global node
    global engine
    board.push(chess.Move.from_uci(move))
    updateBoardDisplay()
    # Update PGN and curMove
    if curMove == "white":
        global curMoveNum
        if curMoveNum == 1:
            node = pgn.add_variation(chess.Move.from_uci(move))
        else:
            node = node.add_variation(chess.Move.from_uci(move))
        curMove = "black"
    else:
        node = node.add_variation(chess.Move.from_uci(move))
        info = engine.analyse(board, chess.engine.Limit(depth=20))
        node.comment = "Score: " + str(info["score"].relative.score())
        curMove = "white"
    eel.updatePgnDisplay(str(pgn))
    curMoveNum += 1
    # Check for continuation of game
    if board.is_stalemate():
        eel.endGame("stalemate")
    elif board.is_insufficient_material():
        eel.endGame("ins_material")
    elif board.is_game_over():
        eel.endGame("checkmate")
    elif board.is_fivefold_repetition():
        eel.endGame("ffr")
    elif board.is_seventyfive_moves():
        eel.endGame("75_moves")
    # Handle next move
    if curMove == "white" and whiteType == "human":
        eel.openMoveInput(curMove)
    elif curMove == "black" and blackType == "human":
        eel.openMoveInput(curMove)
    elif curMove == "white" and whiteType == "engine":
        global whiteEngine
        makeEngineMove(whiteEngine)
    else:
        global blackEngine
        makeEngineMove(blackEngine)

def makeEngineMove(enginePlayer):
    global board
    global curMove
    global pgn
    global node
    global engine
    global engineTime
    eel.closeMoveInput(curMove)
    result = enginePlayer.play(board, chess.engine.Limit(time=engineTime))
    board.push(result.move)
    updateBoardDisplay()
    # Update PGN and curMove
    if curMove == "white":
        global curMoveNum
        if curMoveNum == 1:
            node = pgn.add_variation(result.move)
        else:
            node = node.add_variation(result.move)
        curMove = "black"
    else:
        node = node.add_variation(result.move)
        info = engine.analyse(board, chess.engine.Limit(depth=20))
        node.comment = "Score: " + str(info["score"].relative.score())
        curMove = "white"
    curMoveNum += 1
    eel.updatePgnDisplay(str(pgn))(continueFromEngineMove)

def continueFromEngineMove(x):
    global board
    global curMove
    global pgn
    global node
    global engine
    global engineTime
    # Check for continuation of game
    if board.is_stalemate():
        eel.endGame("stalemate")
    elif board.is_insufficient_material():
        eel.endGame("ins_material")
    elif board.is_game_over():
        eel.endGame("checkmate")
    elif board.is_fivefold_repetition():
        eel.endGame("ffr")
    elif board.is_seventyfive_moves():
        eel.endGame("75_moves")
    # Handle next move
    if curMove == "white" and whiteType == "human":
        eel.openMoveInput(curMove)
    elif curMove == "black" and blackType == "human":
        eel.openMoveInput(curMove)
    elif curMove == "white" and whiteType == "engine":
        global whiteEngine
        makeEngineMove(whiteEngine)
    else:
        global blackEngine
        makeEngineMove(blackEngine)

def updateBoardDisplay():
    global board
    eel.updateBoardDisplay("https://chessboardimage.com/" + urllib.parse.quote(board.fen()) + ".png")

try:
    eel.start("main.html", mode="chrome", size=(1280, 720))
except EnvironmentError:
    if sys.platform in ["win32", "win64"] and int(platform.release()) >= 10:
        eel.start("main.html", mode="edge", size=(1280, 720))
    else:
        raise
