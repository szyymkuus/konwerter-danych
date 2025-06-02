import sys
import os
import json

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

def load_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError as e:
        print(f"Błąd składni JSON w pliku '{path}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Błąd odczytu pliku JSON: {e}")
        sys.exit(1)

def main():
    input_file, output_file = parse_args()

    if input_file.lower().endswith(".json"):
        data = load_json(input_file)
        print("JSON wczytany pomyślnie.")
    else:
        print("Obecnie obsługuje tylko .json")
        sys.exit(1)

if __name__ == "__main__":
    main()
