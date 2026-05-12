
def ip_inputs():
    ip_add = input("Enter IP address: ")
    return ip_add


def ip_classes():
    ip = ip_inputs()
    octets = ip.split('.')

    if len(octets) != 4:
        print("invalid Format")
        return
    try:
        ip_octets = [int(ip_octets) for ip_octets in octets]
    except ValueError:
        print("IP should contain only numbers")
        return
    if not all(0 <= i <= 255 for i in ip_octets):
        print("Each octets must be from 0-255")
        return

    first_octet = ip_octets[0]
    if first_octet == 127:
        print("Loop back Address")
    elif 1 <= first_octet <= 126:
        print("Class A")
    elif 128 <= first_octet <= 191:
        print("Class B")
    elif 192 <= first_octet <= 223:
        print("Class C")
    elif 224 <= first_octet <= 239:
        print("Class D/ Multicast")
    elif 240 <= first_octet <= 255:
        print("Class E/ Experimental")
    else:
        print("Invalid IP Address")


ip_classes()
