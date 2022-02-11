import re
import sys
import csv
import usaddress as usa

if __name__ == '__main__':
    header = ['name', 'address', 'city', 'state', 'zip code', 'country']

    for file_name in sys.argv[1:]:
        print(file_name)
        input_file = open(file_name, 'r')
        list_input_data = input_file.readlines()
        out_file_name = 'parsed_' + file_name.split('.')[0] + '.csv'

        with open(out_file_name, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)


        for address in list_input_data:
            name_other = re.search(r"([A-Za-z- ]*)(.*)", address, re.M)
            out_name = name_other.group(1)
            out_addr = ''
            out_city = ''
            out_state = ''
            out_zip = ''
            out_country = ''

            if name_other.group(1) is not None and name_other.group(2) is not None and len(address) > 7:

                parsed_address = usa.parse(name_other.group(2))
                for item in parsed_address:
                    # print(item)
                    # print(item[1])
                    if item[1] == 'AddressNumber':
                        out_addr += item[0] + ' '
                    if item[1] == 'StreetNamePreDirectional':
                        out_addr += item[0] + ' '
                    if item[1] == 'StreetName':
                        out_addr += item[0] + ' '
                    if item[1] == 'StreetNamePostType':
                        out_addr += item[0] + ' '
                    if item[1] == 'PlaceName':
                        out_city += item[0] + ' '
                    if item[1] == 'StateName':
                        out_state += item[0]
                    if item[1] == 'ZipCode':
                        out_zip += item[0]
                    if item[1] == 'CountryName':
                        out_country += item[0] + ' '

                # print('final out: ' + out_name, out_addr, out_city, out_state, out_zip, out_country)

                with open(out_file_name, 'a', encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    x = [out_name, out_addr, out_city, out_state, out_zip, out_country]
                    # print(x)
                    writer.writerow(x)
            else:
                print('unable to parse: ' + address)