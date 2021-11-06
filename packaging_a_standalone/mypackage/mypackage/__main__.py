import argparse
import sys
from mypackage import capitalize


def main():
    parser = argparse.ArgumentParser(prog='capitalize')
    parser.add_argument('string', nargs='*', help='string to capitalize')
    parser.add_argument('-v', '--version', help='display version', action='version',
                        version=f'%(prog)s 1.0.0')
    args = parser.parse_args()

    if args.string:
        text = ' '.join(word for word in args.string)
        print(capitalize(text))
    else:
        parser.print_usage()
        sys.exit(1)


if __name__ == '__main__':
    sys.exit(main())
