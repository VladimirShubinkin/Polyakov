from ipaddress import ip_network

for i in range(1, 32):
    net1 = ip_network(f'45.218.13.76/{i}', False)
    net2 = ip_network(f'45.218.13.55/{i}', False)
    if net1 != net2:
        print(i)
        break
