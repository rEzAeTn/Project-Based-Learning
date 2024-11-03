![Banner]()

# Monty Hall Problem

The Monty Hall problem is a famous statistical puzzle named after the original host of the game show 'Let's Make a Deal', Monty Hall.
In the game, you are presented with three doors. Behind one door is a **Car**, and behind the other two doors are **Goats**.  After the contestant chooses a door, Monty, who knows what’s behind each door, opens another door which has a goat. The contestant is then given the chance to stick with the original choice or switch to the remaining unopened door.
The question is: "Is it to the contestant’s advantage to switch his choice?"
Hint Statistics and Probabilities : Counter to many people's intuition, the best strategy is to always Switch Choice, as it actually doubles your chances of winning from 1/3 to 2/3.

## Project Overview

The 'Monty Hall Problem Dashboard' is an interactive web application built with Python and Streamlit. It provides a visual and interactive way to understand the Monty Hall problem, a famous statistical puzzle. The dashboard allows users to:

- **Play the Monty Hall Game**: Users can play a single round of the Monty Hall game, choosing a door and then deciding whether to switch after a goat is revealed.

- **Run a Monty Hall Simulation**: Users can run multiple rounds of the Monty Hall game to empirically verify the probabilities associated with the problem. They can specify the number of rounds and whether to switch doors in each round.

By interacting with the dashboard, users can gain a deeper understanding of the Monty Hall problem and the counter-intuitive nature of probability.


## Directory Structure

```
Monty_Hall_Problem/
|-- src/
| |-- main.py
| |-- dashboard.py/
|-- image/
| |-- banner.png
|-- README.md
|-- requirements.txt
```

## Project Structure

- `main.py`: This is a Python module containing the `MontyHallProblem` class. This class includes methods to simulate a single game (`monty_hall_game`) and multiple games (`monty_hall_simulation`) of the Monty Hall problem.

- `dashboard.py`: This is a Python script using Streamlit to create a web app interface for the Monty Hall problem. The user can play the Monty Hall game or run a simulation, choosing whether to switch doors in each round. The results are displayed on the dashboard, allowing the user to understand the probabilities involved in the problem.


## Prerequisites

- Python 3.6 or later
- Streamlit

    - Install Streamlit using pip:
    ```bash
    pip install streamlit
    ```

You can install all the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```


## How To Run
### Run To Local System
- Clone the repository to your local system.
- Open your command line and navigate to the `Monty_Hall_Proble` project directory.
- install necessary dependencies and **Prerequisites**.
- Add the current directory to the `PYTHONPATH`.
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
```
- Run `Password Generator` script.
```bash
python main.py
```
- Run `Dashboard`.
```bash
streamlit run dashboard.py
```

### Run To Google Colab

- How TO Run Streamlit in Google Colab

    1- **Install Streamlit library:**
    ```python
    !pip install -q streamlit
    !pip freeze | grep streamlit
    ```

    2- **Run the Streamlit app in the background:**
    ```python
    !streamlit run app.py &>/dev/null&
    or
    !streamlit run app.py --server.port 8502 &>/dev/null&
    ```

    3- **Install LocalTunnel:**
    ```python
    !npm install localtunnel
    ```

    4- **Get public IP:**
    ```python
    !curl -s http://whatismyip.akamai.com/
    ```
    5- **Run LocalTunnel in the background:**
    ```python
    !npx localtunnel --port 8502
    or
    !nohup npx localtunnel --port 8502 &
    !cat nohup.out
    ```

- Add the current directory to the `PYTHONPATH`. add tis cod to Script
```bash
import sys
sys.path.append('Script Path')
```

## License

This project is licensed under the terms of the MIT license.