import sys


def process_line(line):
    """
    Do some single line processing
    """
    return line


if __name__ == "__main__":
    in_file_name = sys.argv[1]
    out_file_name = sys.argv[2]

    ofile = open(out_file_name, "w", encoding="utf-8")

    with open(in_file_name, encoding="utf-8") as fp:
        for line in fp:
            new_line = process_line(line)
            ofile.write(new_line)

    ofile.close()
