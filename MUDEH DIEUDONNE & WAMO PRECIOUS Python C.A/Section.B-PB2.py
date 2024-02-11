def pay_debt_in_a_year(balance, annual_interest_rate):
    """Calculate the minimum fixed monthly payment needed in order to pay off a credit card balance within 12 months"""
    monthly_interest_rate = annual_interest_rate / 12.0
    minimum_payment = 10
    while True:
        total_paid = minimum_payment * 12
        balance_left = balance
        for month in range(12):
            interest = balance_left * monthly_interest_rate
            payment = min(minimum_payment, balance_left + interest)
            balance_left -= payment
            if balance_left <= 0:
                break
        if balance_left <= 0:
            break
        minimum_payment += 10
    return minimum_payment

# Test the function
print(pay_debt_in_a_year(3329, 0.2))
print(pay_debt_in_a_year(4773, 0.2))
print(pay_debt_in_a_year(3926, 0.2))