import sys
import os


def get_size_files():
    sum_files = 0

    for root, directories, files in os.walk(sys.argv[1]):
        for filename in files:
            bam = os.path.join(root, filename)
            print (bam)
            stateinfo = os.stat(bam)
            sum_files += stateinfo.st_size

        return sum_files / 1024


def main():
    print (get_size_files())


if __name__ == '__main__':
    main()
