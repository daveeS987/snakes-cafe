if __name__ == "__main__":

  print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
''')   

  menu_items={
    "Wings":0,
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
    "Unicorn Tears": 0
  }

  
  def output_response(response: str) -> str:
    if response in menu_items:
      menu_items[response]+=1
      return f'**{menu_items[response]} order of {response} have been added to your meal**'
    elif response == 'quit':
      return "Thank you come again"
    else:
      return f'Please select an item from the list. Check your spelling'

  user_answer=None
  while(user_answer != 'quit'):
    user_answer=input('>')
    print(output_response(user_answer))