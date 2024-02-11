def pay_credit_card_debt(balance, annual_interest_rate, monthly_payment_rate):
    """Calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month"""
    monthly_interest_rate = annual_interest_rate / 12.0
    minimum_monthly_payment = balance * monthly_payment_rate
    total_paid = 0.0
    for month in range(12):
        unpaid_balance = balance - minimum_monthly_payment
        interest = unpaid_balance * monthly_interest_rate
        balance = unpaid_balance + interest
        minimum_monthly_payment = max(balance * monthly_payment_rate, 10)
        total_paid += minimum_monthly_payment
        print("Month: {:02d}  Balance: ${:.2f}  Minimum monthly payment: ${:.2f}  Total paid: ${:.2f}".format(month+1, balance, minimum_monthly_payment, total_paid))
    print("Total paid: ${:.2f}  Remaining balance: ${:.2f}".format(total_paid, balance))

# Test the function
pay_credit_card_debt(5000, 0.18, 0.02)