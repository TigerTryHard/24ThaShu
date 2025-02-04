from browser import document

def start_game(event):
    document["message"].text = "เกมเริ่มต้นแล้ว!"

document["play"].bind("click", start_game)