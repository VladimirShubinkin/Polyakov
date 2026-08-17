from ipaddress import ip_network, ip_address


address = ip_address('111.81.208.27')
max_count = 0
for i in range(1, 32):
    try:
        net = ip_network(f'111.81.192.0/{i}')
        if address in net:
            max_count = max(max_count, net.num_addresses)
    except:
        continue
print(max_count)
