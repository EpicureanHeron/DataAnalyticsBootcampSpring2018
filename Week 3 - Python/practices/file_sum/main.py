with open('myfile.txt', 'r') as text_file:
    sum = 0
    for line in text_file:
        sum += int(line)

    print(f"The sum is: {sum}")