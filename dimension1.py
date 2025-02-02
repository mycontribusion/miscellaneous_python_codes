filename = input('enter the text filename (e.g dimension.txt):  ')
with open(filename, "r") as file:
    dimensions = []
    for line in file:
        words = line.split()
    
        for word in words:
            dimensions.append(word)

width = dimensions[0]
height = dimensions[1]

ratio = int(width)/int(height)

print(f"Good! the width ratio height is {ratio}")

while True:

    desired_width = int(input("enter desired width: "))

    desired_height = desired_width/ratio

    output_text = f'dimension = {desired_width}x{int(desired_height)}'

    lenght_of_text = len(output_text)
    underline = '_'*lenght_of_text

    print(f'\n{underline}')
    print(f'{output_text}\n')
