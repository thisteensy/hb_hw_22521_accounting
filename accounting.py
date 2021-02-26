melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#         )
def underpaid_customers(transaction_file_name):
    '''This function will open a file and for each line in the file it will
    check to see if the customer underpaid and report their name, what they
    paid and what they should have paid'''
    transaction_file = open(transaction_file_name)
    for line in transaction_file:
        transaction_data = line.split("|") # splits the line separated data into elements and assigns them to a list
        name = transaction_data[1] # assigns the elemnt at index 1 to variable name
        num_melons = float(transaction_data[2]) # converts element at index 2 to a float and assigns it to variable named num_melons
        amount_paid = float(transaction_data[3]) # converts element at index 3 to a float and assigns it to variable names amount_paid
        expected_paid = num_melons * melon_cost # calculates the amount that should have been paid
        if amount_paid < expected_paid: # evaluates for underpayment and prints who paid what, what they should have paid and what they owe
            print(f"{name} paid ${amount_paid} but should have paid ${expected_paid:.2f}.\n They owe ${expected_paid - amount_paid:.2f}.") #looked up string formatting here: https://docs.python.org/3/library/string.html
        elif amount_paid > expected_paid: #evaluates for over payment and prints who paid what, what they should have paid and what they are owed in a refund.
            print(f"{name} paid ${amount_paid} but should have paid ${expected_paid:.2f}.\n They are owed a redund of ${amount_paid - expected_paid:.2f}.")

underpaid_customers("customer-orders.txt")  # calls the function with the specific text file