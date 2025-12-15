def main():
    RATE = 2  # ₹ per day
    total = 0
    print("Library Fine Calculator (5 books, ₹2/day late)")
    for i in range(1, 6):
        try:
            s = input(f"Book {i} - days late: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nInput stopped."); break
        try:
            days = int(s)
        except ValueError:
            print("Invalid input, counting as 0."); continue
        if days < 0:
            print("Days cannot be negative."); continue
        if days == 0:
            continue  # on time, no fine
        total += days * RATE
    print(f"Total fine: ₹{total}")

if __name__ == "__main__":
    main()
