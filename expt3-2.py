d1, d2, d3, d4 = 1, 0, 1, 1

p1 = (d1 + d2 + d4) % 2
p2 = (d1 + d3 + d4) % 2
p3 = (d2 + d3 + d4) % 2

hamming = f"{p1}{p2}{d1}{p3}{d2}{d3}{d4}"
print("Hamming Code:", hamming)

#second

h = list("1011101")

p1 = (int(h[0]) + int(h[2]) + int(h[4]) + int(h[6])) % 2
p2 = (int(h[1]) + int(h[2]) + int(h[5]) + int(h[6])) % 2
p3 = (int(h[3]) + int(h[4]) + int(h[5]) + int(h[6])) % 2

error = p1*1 + p2*2 + p3*4

if error != 0:
    print("Error at position:", error)
    h[error-1] = '1' if h[error-1] == '0' else '0'
else:
    print("No error")

print("Corrected Code:", ''.join(h))

#third

d1, d2, d3, d4, d5 = 1, 1, 0, 0, 1


p1 = (d1 + d2 + d4 + d5 + 1) % 2
p2 = (d1 + d3 + d4 + 1) % 2
p4 = (d2 + d3 + d4 + 1) % 2
p8 = (d5 + 1) % 2

hamming = f"{p1}{p2}{d1}{p4}{d2}{d3}{d4}{p8}{d5}"
print("Hamming Code:", hamming)

