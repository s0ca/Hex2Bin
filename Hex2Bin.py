import sys

input_filename = sys.argv[1]
output_filename = sys.argv[2]

file_in = open(input_filename, 'r')
file_out = open(output_filename, 'wb')

outdata = bytes()
for line in file_in:
  data = line.split()
  for d in data:
    if len(d) == 1:
      d = "0" + d
    outdata += bytes.fromhex(d)
file_out.write(outdata)
