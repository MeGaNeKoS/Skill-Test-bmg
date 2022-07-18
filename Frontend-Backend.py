# fizzbuzz challenge
def frontend(n) -> list:
    output = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            output.append("Frontend\nBackend")
        elif i % 3 == 0:
            output.append("Frontend")
        elif i % 5 == 0:
            output.append("Backed")
        else:
            output.append(str(i))
    return output


result = frontend(50)

print(",".join(result))
