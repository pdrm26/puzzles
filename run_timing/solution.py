
def run_timing():
    run_count = 0
    total_time = 0.0
    while True:
        user_input = input(
            "Enter 10 km run time (minutes, or press Enter to finish): ")

        if user_input.strip() == '':
            break

        try:
            run_time = float(user_input)
            if run_time <= 0:
                raise ValueError("Run time must be over Zero")

            total_time += run_time
            run_count += 1
        except ValueError as e:
            print(
                f"Invalid input: {e} Please enter a valid positive number or press Enter.")
            continue

    if run_count == 0:
        print("No run times were entered.")
        return

    print("Average of {avg_time:.2f}, over {run_count} runs".format(
        avg_time=total_time / run_count, run_count=run_count))


if __name__ == "__main__":
    run_timing()
