from argparse import ArgumentParser
import docx


def main(args) -> None:
    input_file, output_file, format_file = process_args(args)
    print("hello")


def process_args(arg_parser: ArgumentParser) -> tuple:
    args_namespace = arg_parser.parse_args()

    output_name: str = args_namespace.output
    format_name: str = args_namespace.format

    try:
        input_name: str = args_namespace.input
        input_file = open(input_name, "r")
    except:
        print("ERROR: unable to open input file")
        # raise

    output_file = open(output_name, "r")

    format_file = open(format_name, "r")

    return (input_file, output_file, format_file)


if __name__ == "__main__":
    args = ArgumentParser(
        prog="Gold IDT Converter",
        description="convert excel spreadsheet into formatted word document",
    )
    args.add_argument("-i", "--input", help="path to excel sheet to import")
    args.add_argument(
        "-o", "--output", help="path to save word doc"
    )  # TODO: add default output file name
    args.add_argument(
        "-f", "--format", help="path to excel sheet format template"
    )  # TODO: add default format

    main(args)
