def check_even_odd():
    n = int(input("Enter a number to check Even/Odd: "))
    if n % 2 == 0:
        return f"{n} is Even"
    return f"{n} is Odd"

def check_prime():
    n = int(input("Enter a number to check Prime: "))
    if n <= 1:
        return f"{n} is Not Prime"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return f"{n} is Not Prime"
    return f"{n} is Prime"

def calculate_average():
    count = int(input("How many numbers do you want to average? "))
    numbers = []
    for _ in range(count):
        val = float(input("Enter number: "))
        numbers.append(val)
    
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    print("\n--- Math Operations Program ---")
    print(check_even_odd())
    print(check_prime())
    print("Calculated Average:", calculate_average())
