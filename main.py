import argparse
from Crypto.Hash import keccak

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-f', '--file', metavar='PATH', required=True,
                        help='Path to the file where students names are stored.')
    parser.add_argument('-n', '--numbilets', metavar='NUMER_OF_TICKETS', type=int,
                        required=True, help='Number of exam tickets.')
    parser.add_argument('-p', '--parameter', metavar='PARAMETER', type=int,
                        required=True, help='Parameter of distribution.')

    args = parser.parse_args()

    students_names = []
    with open(args.file, encoding='utf-8', mode='r') as file:
        for line in file.readlines():
            while line.endswith('\n') or line.endswith('\r'):
                line = line[:-1]
            students_names.append(line)
    
    for student in students_names:
        data = (student + str(args.parameter)).encode('utf-8')
        hash_hex = keccak.new(digest_bits=256, data=data).hexdigest()
        hash_decimal = int(hash_hex, base=16)
        ticket_id = (hash_decimal % args.numbilets) + 1
        print('{}: {}'.format(student, ticket_id))
    

if __name__ == '__main__':
    main()
