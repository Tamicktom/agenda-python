def format_cellphone(phone_number: str):
    if len(phone_number) == 11:
        return f'({phone_number[0:2]}) {phone_number[2:7]}-{phone_number[7:11]}'
    return f'({phone_number[0:2]}) {phone_number[2:6]}-{phone_number[6:10]}'