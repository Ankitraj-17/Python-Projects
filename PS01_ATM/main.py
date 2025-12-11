def main():
    bal = 0.0
    while True:
        try:
            ch = input("\n1) Deposit  2) Withdraw  3) Check Balance  4) Exit\nChoose: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye."); break

        if ch == "1":
            try:
                amt = float(input("Deposit amount: "))
            except ValueError:
                print("Invalid amount."); continue 
            if amt <= 0:
                print("Enter a positive amount."); continue
            bal += amt; print(f"Deposited {amt:.2f}. Balance: {bal:.2f}")

        elif ch == "2":
            try:
                amt = float(input("Withdraw amount: "))
            except ValueError:
                print("Invalid amount."); continue
            if amt <= 0:
                print("Enter a positive amount."); continue
            if amt > bal:
                print("Insufficient funds. Skipping."); continue
            bal -= amt; print(f"Withdrew {amt:.2f}. Balance: {bal:.2f}")

        elif ch == "3":
            print(f"Balance: {bal:.2f}")

        elif ch == "4":
            print("Goodbye."); break

        else:
            print("Enter 1-4.")

if __name__ == "__main__":
    main()
    print("ATM session ended.")
