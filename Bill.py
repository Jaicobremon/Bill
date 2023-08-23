# A Project by Jaicob Remon

# Import necessary libraries
import tkinter as tk  # Library for creating GUI applications
import yfinance as yf  # Library for fetching stock prices
import math  # Library for mathematical operations

# Define the ChatBot class
class ChatBot:
    def __init__(self):
        # Initialize bot attributes
        self.bot_name = "Bill"
        self.options = {
            "1": self.calculator,
            "2": self.stock_prices,
            "3": self.password_grader,
            "4": self.end_program,
        }

    # Greet the user
    def greet_user(self):
        print(f"Hi, I am {self.bot_name} :)")  # Greeting message
        print("What can I do for you?")

    # Function to create a calculator GUI
    def calculator(self):
        # Function to evaluate mathematical expressions
        def evaluate_expression():
            try:
                result = eval(entry.get())  # Evaluate the expression
                result_label.config(text="Result: " + str(result))  # Display the result
            except Exception as e:
                result_label.config(text="Invalid expression")

        # Create the main window for the calculator GUI
        root = tk.Tk()
        root.title("Simple Calculator")

        # Create an entry widget for user input
        entry = tk.Entry(root, width=30)
        entry.pack(pady=10)

        # Create a button to evaluate expressions
        calculate_button = tk.Button(root, text="Calculate", command=evaluate_expression)
        calculate_button.pack()

        # Create a label to display the result
        result_label = tk.Label(root, text="Result:")
        result_label.pack(pady=10)

        root.mainloop()  # Run the GUI loop
        self.options_menu()

    # Function to fetch live stock prices
    def stock_prices(self):
        # Function to fetch the live stock price using Yahoo Finance API
        def fetch_live_stock_price(ticker_symbol):
            try:
                stock = yf.Ticker(ticker_symbol)
                live_price = stock.history(period="1d")["Close"].iloc[0]
                return live_price
            except:
                return None

        # Get user input for stock symbol
        ticker_symbol = input("Enter the stock symbol (e.g., AAPL): ")

        # Fetch live stock price
        live_price = fetch_live_stock_price(ticker_symbol)
        if live_price is not None:
            print(f"The live price of {ticker_symbol} is ${live_price:.2f} USD")
        else:
            print(f"We were unable to find information on '{ticker_symbol}'")

        self.options_menu()

    # Function to estimate password strength using brute force time estimation
    def password_grader(self):
        # Function to estimate time to crack a password
        def estimate_crack_time(password):
            lowercase_letters = 26
            uppercase_letters = 26
            digits = 10
            special_characters = 33
            total_characters = lowercase_letters + uppercase_letters + digits + special_characters

            password_length = len(password)
            possible_combinations = math.pow(total_characters, password_length)

            attack_rate = 1e9  # 1 billion guesses per second
            seconds_to_crack = possible_combinations / attack_rate
            return seconds_to_crack

        # Get user input for password
        password = input("Enter a password to estimate its crack time: ")

        # Estimate and display time to crack password
        crack_time = estimate_crack_time(password)
        if crack_time < 1:
            print("Estimated time to crack: less than a second")
        elif crack_time < 60:
            print(f"Estimated time to crack: {crack_time:.2f} seconds")
        elif crack_time < 3600:
            print(f"Estimated time to crack: {crack_time/60:.2f} minutes")
        elif crack_time < 86400:
            print(f"Estimated time to crack: {crack_time/3600:.2f} hours")
        else:
            print(f"Estimated time to crack: {crack_time/86400:.2f} days")

        self.options_menu()

    # Function to end the program
    def end_program(self):
        print("Thank you for using the program. Goodbye !")
        watermark = '''
        JJJJJJJJ     RRRRRRRRRR
            JJ       RR      RR
            JJ       RR      RR
            JJ       RRRRRRRRRR
        J   JJ       RR   RR
        JJJJ         RR    RR
        '''
        print(watermark)
        exit()

    # Function to display options and handle user input
    def options_menu(self):
        options_list = '''
        1. Calculator
        2. Live Stock Prices
        3. Password Grading System
        4. End Program

        Type in the number for your selected choice
        '''
        print(options_list)
        question = input("Which option do you want: ")

        # Check user input against available options
        if question in self.options:
            self.options[question]()  # Execute the chosen option
        else:
            print("Invalid option. Please select a valid option.")
            self.options_menu()  # Display options again

    # Function to run the chatbot
    def run(self):
        self.greet_user()  # Greet the user
        self.options_menu()  # Display options

# Create an instance of the ChatBot class and run it
chat_bot = ChatBot()
chat_bot.run()