from sys import argv

script_name, hours, rate, prize = argv

print(f'Empoyers salary: {float(hours) * float(rate) + float(prize)}')