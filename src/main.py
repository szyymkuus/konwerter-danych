import sys
import os

def parse_args():
    if len(sys.argv) != 3:
        print("Użycie: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.isfile(input_path):
        print(f"Błąd: plik wejściowy '{input_path}' nie istnieje.")
        sys.exit(1)

    return input_path, output_path

def main():
    input_file, output_file = parse_args()
    print(f"Wczytano plik wejściowy: {input_file}")
    print(f"Plik wyjściowy: {output_file}")

if __name__ == "__main__":
    main()