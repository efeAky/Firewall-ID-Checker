# Validate input format (ValueError)
# If input is empty, raise ValueError
# If the last 6 characters are not digits, raise ValueError

# Validate firewall integrity (FirewallBreachError)
# If the input does not start with "FW", raise FirewallBreachError
# If length is not exactly 8 characters, raise FirewallBreachError

# Function to decrypt the stored firewall key
def decrypt_key(key_attempt):
    # Store the encrypted key in reversed order
    encryption_key = "654321WF"
    # Decrypt the key by reversing it
    decrypted_key = encryption_key[::-1]
    # Compare decrypted key with user input
    if decrypted_key == key_attempt:
        print("Firewall ID is valid!")   # Valid input message
        print("Access Granted!")         # Access granted message
        return True                      # Return True if valid
    else:
        print("Invalid Firewall ID!")   # Invalid input message
        return False                     # Return False if invalid


# Custom exception class for corrupted firewall ID
class FireWallBreachError(Exception):
    pass

# Maximum number of allowed attempts
MAX_ATTEMPT = 5
# Initialize attempt counter
attempt = 1

# Loop to repeatedly ask for user input
while True:
    # Check if attempts are within the allowed limit
    if attempt <= MAX_ATTEMPT:
        try:
            print(f"Attempt {attempt} to access the Firewall")
            # Prompt user to enter the firewall ID
            firewall_id = input("Enter the firewall id: ")

            # Check if input is empty (ValueError)
            if not firewall_id:
                raise ValueError("It cannot be empty!")

            # Check if input length is exactly 8 characters (FirewallBreachError)
            if len(firewall_id) != 8:
                raise FireWallBreachError("It must contain 8 characters!")

            # Check if input starts with "FW" (FirewallBreachError)
            letter_part = firewall_id[0:2]
            if letter_part != "FW":
                raise FireWallBreachError("It must start with FW!")

            # Check if last 6 characters are digits (ValueError)
            numeric_part = firewall_id[2:]
            if not numeric_part.isdigit():
                raise ValueError("Last 6 characters must be digits!")

            # Validate input against decrypted key
            if decrypt_key(firewall_id):
                break  # Exit loop if valid

        # Handle ValueError exceptions
        except ValueError as ve:
            print("ValueError:", ve)

        # Handle FirewallBreachError exceptions
        except FireWallBreachError as fe:
            print("FirewallBreachError:", fe)

        # Finally block to increment attempt counter
        finally:
            attempt += 1

    # If attempts exceed maximum, deny access and exit loop
    else:
        print("Maximum attempts reached. Access denied.")
        break
