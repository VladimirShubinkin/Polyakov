from ipaddress import ip_network


def check(net):
    for address in net:
        bin_address = f'{address:b}'
        if not bin_address[:16].count('0') < bin_address[16:].count('0'):
            return False
    return True


for a in range(255, -1, -1):
    net = ip_network(f'159.242.{a}.223/255.255.254.0', False)
    if check(net):
        print(a)
        break
