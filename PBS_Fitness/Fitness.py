def main(goal=10_000):
    total, hour = 0, 1
    print(f"Fitness Tracker: Step Goal Monitor (goal: {goal})")
    while True:
        try:
            s = input(f"Hour {hour} steps: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nSession ended."); break

        try:
            steps = int(s)
        except ValueError:
            print("Enter a whole number."); continue
        if steps < 0:
            print("Steps cannot be negative."); continue

        total += steps
        print(f"Total so far: {total}")

        if total >= goal:
            print(f"Goal reached! {total} steps in {hour} hour(s).")
            break  # stop and report success

        hour += 1

if __name__ == "__main__":
    main()
