# cat checkbook.py
class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the account.
        Args:
            amount: The amount to deposit (must be positive)
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        Args:
            amount: The amount to withdraw
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Display the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))


def get_valid_float(prompt):
    """
    Prompts the user for a valid float input.
    Continues to ask until a valid number is entered.
    
    Args:
        prompt: The message to display to the user
        
    Returns:
        A valid float value
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Amount cannot be negative. Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")


def get_valid_action():
    """
    Prompts the user for a valid action choice.
    Continues to ask until a valid option is selected.
    
    Returns:
        A valid action string (lowercase)
    """
    valid_actions = ['deposit', 'withdraw', 'balance', 'exit']
    
    while True:
        try:
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
            
            if action in valid_actions:
                return action
            else:
                print("Invalid command. Please choose from: deposit, withdraw, balance, or exit.")
        except EOFError:
            print("\nInput stream ended. Exiting program.")
            return 'exit'
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting.")
            return 'exit'
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")


def main():
    """Main function to run the checkbook program."""
    cb = Checkbook()
    print("Welcome to your Checkbook Manager!")
    print("-" * 40)
    
    while True:
        try:
            action = get_valid_action()
            
            if action == 'exit':
                print("Thank you for using Checkbook Manager. Goodbye!")
                break
                
            elif action == 'deposit':
                amount = get_valid_float("Enter the amount to deposit: $")
                cb.deposit(amount)
                
            elif action == 'withdraw':
                amount = get_valid_float("Enter the amount to withdraw: $")
                cb.withdraw(amount)
                
            elif action == 'balance':
                cb.get_balance()
                
            print()  # Add blank line for readability
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting gracefully...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("The program will continue. Please try again.")
            print()


if __name__ == "__main__":
    main()