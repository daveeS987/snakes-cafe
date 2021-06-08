from print_menu import print_menu

menu_items = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0,
}


def get_summary(obj):
    result = ""
    for item in obj:
        if obj[item] > 0:
            result += f"{obj[item]} {item} \n"
    return result


def output_response(response: str) -> str:
    if response in menu_items:
        menu_items[response] += 1
        return f"**{menu_items[response]} order of {response} have been added to your meal**"
    elif response == "summary":
        summary = get_summary(menu_items)
        return f"""
*-----------------------------  Summary  -----------------------------*\n
{summary}
      """

    elif response == "quit":
        return "Thank you come again"
    else:
        return f"Please select an item from the list. Check your spelling"


def main():
    print_menu()
    user_answer = None
    while user_answer != "quit":
        user_answer = input(">")
        print(output_response(user_answer))


if __name__ == "__main__":
    main()
