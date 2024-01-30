

if __name__ == "__main__":
    inputs = []
    for i in range(5):
        num = int(input(f"Digite o numero {i + 1}: "))
        inputs.append(num)

    results = []
    for i in range(0, 4):
        results.append(inputs[i] + inputs[i+1])

    print(f"Min: {min(results)}")
    print(f"Max: {max(results)}")
