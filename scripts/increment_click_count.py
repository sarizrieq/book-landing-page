def increment_click_count(file_path):
    try:
        # Read the current count
        with open(file_path, 'r') as file:
            count = int(file.read().strip())

        # Increment the count
        count += 1

        # Write the updated count back to the file
        with open(file_path, 'w') as file:
            file.write(str(count))

        return count
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    count = increment_click_count("click_count.txt")
    if count is not None:
        print(f"Button has been clicked {count} times.")
