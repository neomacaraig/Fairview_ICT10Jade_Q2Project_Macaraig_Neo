from pyscript import document, display, HTML

# define four grade level sets
grade_7 = {"Bobby Brown", "Jones Descartes"}
grade_8 = {"Patrick Jane", "Prince Hamilton"}
grade_9 = {"Fiona Ramirez", "Harvey Specter"}
grade_10 = {"Caleb Espia", "Nelson Velasco"}

# combine the four grade sets into the master set using the union operator (|)
master_set = grade_7 | grade_8 | grade_9 | grade_10

def add_member(event):
    # get values from input text box and capitalize first letter of first and last name
    fname = document.getElementById("fname").value.strip().capitalize()
    lname = document.getElementById("lname").value.strip().capitalize()

    if not fname and not lname:
        return

    full_name = f"{fname} {lname}".strip()
    master_set.add(full_name)

    total = len(master_set)
    members_list = "</li><li>".join(master_set)

    output_text = f"<b>Total Members: {total}</b><br><ul style='text-align: left; margin: 10px 0 0 0; padding-left: 20px;'><li>{members_list}</li></ul>"

    display(HTML(output_text), target="output1", append=False)