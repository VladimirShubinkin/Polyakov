from ipaddress import ip_network

net = ip_network('112.208.0.0/255.255.128.0')
count = 0
for address in net:
    bin_address = f'{address:b}'
    if bin_address.count('1') % 11 == 0:
        count += 1
print(count)


from math import comb as C

print(C(15, 5))
