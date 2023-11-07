# Автор В.Н. Шубинкин

from ipaddress import ip_network

count = 0
for address in ip_network('202.75.38.176/255.255.255.240', False):
    bin_address = f'{address:b}'
    count += '111' not in bin_address and '000' not in bin_address
print(count)
