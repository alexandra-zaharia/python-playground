import argparse
from datetime import datetime
import os
import runpy
import sys
from mypackage import capitalize


def now():
    return datetime.now().strftime('%Y-%m-%d %H:%m:%S')


def runner():
    version = '1.0.0'
    parser = argparse.ArgumentParser(prog='runner')
    parser.add_argument('script', help='Python script to run')
    parser.add_argument('-v', '--version', help='display version', action='version',
                        version=f'%(prog)s {version}')
    args = parser.parse_args()

    if args.script:
        print(f'{parser.prog} v{version} started on {now()}')
        # exec(open(args.script).read())
        exec(compile(open(args.script).read(), os.path.basename(args.script), 'exec'))
        # argparse.Namespace(**runpy.run_path(args.script))
        print(f'{parser.prog} v{version} finished on {now()}')
    else:
        parser.print_usage()
        sys.exit(1)


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