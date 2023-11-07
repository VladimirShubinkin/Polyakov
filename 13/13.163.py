# Автор В.Н. Шубинкин

from ipaddress import ip_network

count = 0
for address in ip_network('184.178.54.144/255.255.255.240', False):
    bin_address = f'{address:b}'
    count += '111' in bin_address
print(count)