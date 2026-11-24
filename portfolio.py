from pyscript import document
from pyodide.ffi import create_proxy

cards = [
    ("#card-drill2", "sets"),
    ("#card-sw1", "sets"),
    ("#card-skillstest", "dicts"),
    ("#card-creator", "about"),
]

def filter_cards(filter_type):
    for card_id, category in cards:
        card = document.querySelector(card_id)
        if card:
            if filter_type == "all" or category == filter_type:
                card.style.display = ""
            else:
                card.style.display = "none"

def set_active_button(active_id):
    for btn_id in ["#btn-all", "#btn-sets", "#btn-dicts", "#btn-about"]:
        btn = document.querySelector(btn_id)
        if btn:
            if btn_id == active_id:
                btn.classList.add("active")
            else:
                btn.classList.remove("active")

def on_all(event):
    set_active_button("#btn-all")
    filter_cards("all")

def on_sets(event):
    set_active_button("#btn-sets")
    filter_cards("sets")

def on_dicts(event):
    set_active_button("#btn-dicts")
    filter_cards("dicts")

def on_about(event):
    set_active_button("#btn-about")
    filter_cards("about")

document.querySelector("#btn-all").addEventListener("click", create_proxy(on_all))
document.querySelector("#btn-sets").addEventListener("click", create_proxy(on_sets))
document.querySelector("#btn-dicts").addEventListener("click", create_proxy(on_dicts))
document.querySelector("#btn-about").addEventListener("click", create_proxy(on_about))