# Автор В.Н. Шубинкин

from ipaddress import ip_network

count = 0
for address in ip_network('192.168.248.176/255.255.255.240', False):
    bin_address = f'{address:b}'
    count += bin_address.count('1') == bin_address.count('0')
print(count)
