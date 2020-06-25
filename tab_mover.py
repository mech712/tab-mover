import argparse, time
import clipboard
import pynput

class Const:
    DELAY=0.1
    STOP_WORD="saved"

def copy(args):
    print("copy")
    urls = []

    switch_browser()
    while True:
        move_address_line()
        #скопировать
        ctrl_c()
        address_line = clipboard.paste()
        #если saved то брейк
        if address_line==Const.STOP_WORD: break
        #занести в список
        urls.append(address_line)
        #вставить saved
        clipboard.copy(Const.STOP_WORD)
        ctrl_v()
        #следующая вкладка
        next_tab()
    print(urls)
    urls_text = "\n".join(urls)
    with open("urls.txt",mode="w") as file:
        file.write(urls_text)
    print("urls.txt saved")
        

def paste(args):
    print("paste")
    switch_browser()
    urls_text=""
    with open("urls.txt", mode="r") as file:
        urls_text = file.read()
    urls = urls_text.split("\n")
    for url in urls:
        new_tab()
        move_address_line()
        clipboard.copy(url)
        ctrl_v()
        press_enter()

    print("tabs opened")



def switch_browser():
    kb = pynput.keyboard.Controller()
    kb.press(pynput.keyboard.Key.alt)
    kb.press(pynput.keyboard.Key.tab)
    kb.release(pynput.keyboard.Key.tab)
    kb.release(pynput.keyboard.Key.alt)
    time.sleep(Const.DELAY)


def move_address_line():
    kb = pynput.keyboard.Controller()
    kb.press(pynput.keyboard.Key.ctrl)
    kb.press('l')
    kb.release('l')
    kb.release(pynput.keyboard.Key.ctrl)
    time.sleep(Const.DELAY)

def ctrl_c():
    kb = pynput.keyboard.Controller()
    kb.press(pynput.keyboard.Key.ctrl)
    kb.press('c')
    kb.release('c')
    kb.release(pynput.keyboard.Key.ctrl)
    time.sleep(Const.DELAY)

def ctrl_v():
    kb = pynput.keyboard.Controller()
    kb.press(pynput.keyboard.Key.ctrl)
    kb.press('v')
    kb.release('v')
    kb.release(pynput.keyboard.Key.ctrl)
    time.sleep(Const.DELAY)

def press_enter():
    kb = pynput.keyboard.Controller()
    kb.press(pynput.keyboard.Key.enter)
    kb.release(pynput.keyboard.Key.enter)
    time.sleep(Const.DELAY)

def next_tab():
    kb = pynput.keyboard.Controller()
    kb.press(pynput.keyboard.Key.ctrl)
    kb.press(pynput.keyboard.Key.tab)
    kb.release(pynput.keyboard.Key.tab)
    kb.release(pynput.keyboard.Key.ctrl)
    time.sleep(Const.DELAY)

def new_tab():
    kb = pynput.keyboard.Controller()
    kb.press(pynput.keyboard.Key.ctrl)
    kb.press("t")
    kb.release("t")
    kb.release(pynput.keyboard.Key.ctrl)
    time.sleep(Const.DELAY)

def main():
    print("**** Tab Mover works ****")
    parser = argparse.ArgumentParser(description='move tabs from one browser window to another browser window')
    subparsers = parser.add_subparsers()
    
    copy_parser=subparsers.add_parser("copy")
    copy_parser.set_defaults(func=copy)

    paste_parser=subparsers.add_parser("paste")
    paste_parser.set_defaults(func=paste)
    
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()