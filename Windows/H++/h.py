import sys

def interpret_hpp(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    value = 0
    output = []

    for char in code:
        if char == 'h':
            value += 1
        elif char == 'H':
            if value > 0:
                output.append(chr(value))
            value = 0

    return ''.join(output)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python h.py <filename.hhh>")
        sys.exit(1)

    file_path = sys.argv[1]
    result = interpret_hpp(file_path)

    if result:
        print(result)
    else:
        print("No output generated.")
