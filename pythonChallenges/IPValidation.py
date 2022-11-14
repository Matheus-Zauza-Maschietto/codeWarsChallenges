"""Função que verifica a validade de um ip, considerando que ele deva ter 4 octetos entre 0 e 255"""

def is_valid_IP(string):
    return all(item is True for item in [True if ip.strip() != '' and ip.isdigit() and (True if len(ip) > 1 and ip[0] != '0' else True if len(ip) == 1 else False) and 255 >= int(ip.strip()) and len(string.split('.')) == 4 >= 0 else False for ip in string.split('.')])


print(is_valid_IP(''))

