from browser import document, window

def start_game(event):
    document["message"].text = "เกมเริ่มต้นแล้ว!"
    # เรียกฟังก์ชันจากไฟล์เกม 24code.py
    window.start_24game()  # ฟังก์ชันที่ต้องมีใน 24code.py

document["play"].bind("click", start_game)