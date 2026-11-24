from pyscript import document, when

notes = [
    "Drill 2 uses Python set union (|) and .update() to merge grade-level rosters.",
    "Seatwork 1 normalizes names with .strip() and .title() before checking membership against the Math Club list.",
    "The Skills Test stores non-metal element data inside a dictionary for quick symbol lookups.",
    "This portfolio ties all outputs into one using pyscript."
]

current_index = -1

@when("click", "#nextFactBtn")
def cycle_note(event):
    global current_index
    current_index = (current_index + 1) % len(notes)
    document.querySelector("#creatorFact").innerText = notes[current_index]