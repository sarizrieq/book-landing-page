def increment_click_count():
    try:
        # Read the current count
        with open('counter.txt', 'r') as file:
            count = int(file.read().strip())
    except FileNotFoundError:
        count = 0  # If the file doesn't exist, start from 0

    # Increment the count
    count += 1

    # Write the new count back to the file
    with open('counter.txt', 'w') as file:
        file.write(str(count))

if __name__ == "__main__":
    increment_click_count()
