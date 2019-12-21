import sys

s = int(sys.argv[3])
m = int(sys.argv[4]) + s
i = 0
write = False
with open(sys.argv[1], 'r') as infile:
    with open(sys.argv[2], 'w') as outfile:
        for line in infile:
            if(line.strip() == ''):
                if(write):
                    outfile.write('\n')
                i += 1
                if(i >= m):
                    break
            elif(i >= s):
                arr = line.strip().split('\t')
                if(len(arr) == 2):
                    text = arr[0].replace('İ', 'i').replace('I', 'ı').replace('Ğ', 'ğ').replace('Ü', 'ü').replace('Ş', 'ş').replace('Ö', 'ö').replace('Ç', 'ç').lower().strip()
                    tag = arr[1].replace('ORGANIZATION', 'ORG').replace('LOCATION', 'LOC').replace('PERSON', 'PER').strip()
                    outfile.write('{} {}\n'.format(text, tag))
                    write = True
 