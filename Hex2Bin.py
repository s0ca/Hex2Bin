import sys

def convert_hex_to_bytes(input_filename, output_filename):
    with open(input_filename, 'r') as file_in, open(output_filename, 'wb') as file_out:
        outdata = bytearray()
        for line in file_in:
            data = line.split()
            for d in data:
                if len(d) == 1:
                    d = "0" + d
                outdata.extend(bytes.fromhex(d))
        file_out.write(outdata)

if __name__ == "__main__":
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    convert_hex_to_bytes(input_filename, output_filename)
