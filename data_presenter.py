open_file = open('CupcakeInvoices.csv')

# for line in open_file:
#     print(line)

# for line in open_file:
#     line = line.strip()
#     type = line.split(',')
#     print(type[2])

# for line in open_file:
#     line = line.strip()
#     value = line.split(',')
#     total = float(value[3])*float(value[4])
#     print(total)

total = 0

for line in open_file:
    line = line.strip()
    value = line.split(',')
    total = total + float(value[3])*float(value[4])
print(total)

open_file.close()
