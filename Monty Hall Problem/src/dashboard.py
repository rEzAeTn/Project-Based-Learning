import time

import streamlit as st
from PIL import Image

from src.main import MontyHallProblem

# Set the title of the Streamlit app
title = '<h1 style="text-align: center; color: SkyBlue; font-size: 50px;">Monty Hall Problem</h1>'
st.markdown(title, unsafe_allow_html=True)

# Load the banner image
image = Image.open('image/banner.png')
st.image(image)

# Create an instance of the MontyHallProblem
monty_hall = MontyHallProblem()
game = None
simulation = None

# Create a selectbox for the user to choose between Game and Simulation
mode = st.selectbox(
  ":blue[**Game or Simulation**]",
  ('Select Mode ...', 'Game', 'Simulation')
)

if mode == 'Game':
    # Ask the user to choose a door
    user_choice = st.selectbox(
      ":blue[**Choose a Door**]",
      ('Select Door ...', 'Door 1', 'Door 2', 'Door 3')
    )

    if user_choice != 'Select Door ...':
      # Convert the door choice to an index
      user_choice = int(user_choice[-1]) - 1

      # Get Switch or Keep Choice from User
      col1, col2, col3, col4 = st.columns(4)
      switch_choice = col2.button("**:green[Switch] Choice**")
      keep_choice = col3.button("**:red[Keep] Choice**")

      # Run the game based on user's choice
      if switch_choice:
        game = monty_hall.monty_hall_game(initial_choice=user_choice, switch_choice=True)
      elif keep_choice:
        game = monty_hall.monty_hall_game(initial_choice=user_choice, switch_choice=False)

      # Display the result of the game
      if game is not None:
        door_revealed = monty_hall.door_revealed
        st.write(f"Door Revealed {door_revealed + 1}: :red[**Goat**]")

        if game:
          st.success(":rainbow[**Congratulations! You won the :green[Car]**]")
        else:
          st.error("**Oops, you got a :red[Goat]**")

        # Add a button to play again
        if st.button('Play Again'):
          # :TODO - Reset all variables and widgets
          # This will rerun the script from the top
          st.rerun()

if mode == 'Simulation':
  # Get the number of games to simulate from the user
  number_of_repeat = st.number_input(
    "**Enter Number of :blue[Game] to :blue[Simulation]**",
    min_value=0, max_value=100000,
    value=0
  )

  # Run the simulation if the number of games is greater than 0
  if number_of_repeat > 0:
      col1, col2, col3, col4 = st.columns(4)

      # Get Switch or Keep Choice from User
      with_switch = col2.checkbox("**:orange[With] Switching**")
      without_switch = col3.checkbox("**:orange[Without] Switching**")

      # Run the simulation with switching
      if with_switch:
        col1, col2 = st.columns(2)
        col1.subheader("**Number of :green[Wins] :orange[With] switching**")
        col2.subheader("**Number of :red[Losses] :orange[With] switching**")

        chart1 = col1.line_chart(x=None, y=None, width=200, height=400)
        chart2 = col2.line_chart(x=None, y=None, width=200, height=400)

        num_of_wins = 0
        num_of_losses = 0

        for i in range(number_of_repeat):
          win_with_switching, lost_with_switching = monty_hall.monty_hall_simulation(number_of_round=1, switch_choice=True)
          num_of_wins += win_with_switching
          num_of_losses += lost_with_switching

          chart1.add_rows([num_of_wins/ (i + 1)])
          chart2.add_rows([num_of_losses / (i + 1)])

          time.sleep(0.01)

      # Run the simulation without switching
      if without_switch:
        col1, col2 = st.columns(2)
        col1.subheader("**Number of :green[Wins] :orange[Without] switching**")
        col2.subheader("**Number of :red[Losses] :orange[Without] switching**")

        chart1 = col1.line_chart(x=None, y=None, width=200, height=400)
        chart2 = col2.line_chart(x=None, y=None, width=200, height=400)

        num_of_wins = 0
        num_of_losses = 0

        for i in range(number_of_repeat):
          win_without_switching, lost_without_switching = monty_hall.mo
          nty_hall_simulation(number_of_round=1, switch_choice=False)
          num_of_wins += win_without_switching
          num_of_losses += lost_without_switching

          chart1.add_rows([num_of_wins/ (i + 1)])
          chart2.add_rows([num_of_losses / (i + 1)])

          time.sleep(0.01)
