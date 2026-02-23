def withdraw(accounts, card_number, amount):
    if card_number not in accounts:
        return "Card Not Found"
    
    current_balance = accounts[card_number]
    if current_balance < amount:
        return "Insufficient Funds"
    
    new_balance = float(current_balance - amount)
    accounts[card_number] = new_balance
    return accounts[card_number]  

accounts = {
    "4111-1111": 500.00,
    "4222-2222": 80.00,
}
print(withdraw(accounts, "4111-1111", 200.00))
print(withdraw(accounts, "4222-2222", 100.00))
print(withdraw(accounts, "9999-0000", 50.00))
