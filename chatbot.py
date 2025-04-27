import datetime

name = input("What is your name:: ")

# Greeting messages
currtime = datetime.datetime.now().hour
if currtime < 12:
    print("Good morning", name)
elif 12 <= currtime < 17:
    print("Good afternoon", name)
elif 17 <= currtime < 21:
    print("Good evening", name)
else:
    print("Good night", name)

print("Hello! How can I assist you today?")

# Initialize count dictionary
option_count = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0
}

# Chatbot display options
while True:
    print("\n1. Order Tracking & Status Updates")
    print("2. FAQ & Customer Support")
    print("3. Offers & Discounts")
    print("4. Language Support")
    print("5. Payment & Checkout Assistance")
    print("6. Exit")

    option = input("Please select an option (1-6): ")

    # Handle Exit
    if option == "6":
        print("Thank you for using our chatbot!")
        break

    # Check if option is valid and in counting system
    if option in option_count:
        option_count[option] += 1  # Increase the counter

        # If limit reached, exit
        if option_count[option] > 3:
            print("You have reached the maximum number of tries for option " + option + ". Exiting the chatbot.")
            break

        # Handle options
        if option == "1":
            orderno = input("Enter your order number: ")
            print("Checking status for order " + orderno + "...")
            print("Your order is on the way.")
        
        elif option == "2":
            print("\nFAQ & Customer Support:")
            print("1. Refund Policy")
            print("2. Shipping Details")
            print("3. Product Information")
            print("4. Speak to a Customer Care")
            faqoption = input("Please select a topic (1-4): ")
            print("Redirecting to the support section...")
        
        elif option == "3":
            print("\nOffers & Discounts:")
            print("Checking for deals based on your purchase history...")
            print("You have 10% discount available on next purchase!")
        
        elif option == "4":
            lang = input("Which language do you prefer to continue? ")
            print("Switching to " + lang + "...")
            print("Language updated successfully.")
        
        elif option == "5":
            print("\nPayment & Checkout Assistance:")
            print("1. Help with Payment Process")
            print("2. Apply Promo Code")
            print("3. Solve Payment Issues")
            print("4. View Available Payment Options")
            payment_option = input("Please select an option (1-4): ")
            print("Processing your request...")

    else:
        print("Invalid option. Please try again.")
