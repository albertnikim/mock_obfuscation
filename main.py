import argparse


def generate_asterisk(line):
    variants_asterisk = []

    for i in range(1, len(line)-1):
        variant_inside = line[0] + '*' * i + line[i+1:]
        variants_asterisk.append(variant_inside)

        variant_backward = line[:-i] + '*' * i
        variants_asterisk.append(variant_backward)

        variant_forward = '*' * i + line[i:]
        variants_asterisk.append(variant_forward)

    return variants_asterisk


def process_files(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.read().splitlines()

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            variants_asterisk = ', '.join(map(str, generate_asterisk(line)))
            outfile.write(f"{line}\t{variants_asterisk}\n")


def main():
    parser = argparse.ArgumentParser(description='process the file')
    parser.add_argument('--input', dest='input_file', required=True, help='the file to be processed')
    parser.add_argument('--output', dest='output_file', required=True, help='the obfuscated file')
    args = parser.parse_args()
    process_files(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
