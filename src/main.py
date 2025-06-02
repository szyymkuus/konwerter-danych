import sys
import os
import json
import yaml

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

def save_json(data, path):
    """
    Zapisuje obiekt (data) do pliku JSON zgodnie ze standardową składnią.
    """
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Dane zapisano do JSON w '{path}'.")
    except Exception as e:
        print(f"Błąd zapisu pliku JSON: {e}")
        sys.exit(1)

def load_yaml(path):
    """
    Wczytuje dane z pliku YAML (lub YML) i waliduje składnię.
    Zwraca wczytany obiekt (zwykle dict/list).
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data
    except yaml.YAMLError as e:
        print(f"Błąd składni YAML w pliku '{path}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Błąd odczytu pliku YAML: {e}")
        sys.exit(1)

def save_yaml(data, path):
    """
    Zapisuje obiekt (data) do pliku YAML (lub YML) zgodnie z poprawną składnią.
    """
    try:
        with open(path, 'w', encoding='utf-8') as f:
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)
        print(f"Dane zapisano do YAML w '{path}'.")
    except Exception as e:
        print(f"Błąd zapisu pliku YAML: {e}")
        sys.exit(1)


def main():
    input_file, output_file = parse_args()

    # Wczytywanie wejścia
    if input_file.lower().endswith(".json"):
        data = load_json(input_file)
        print("JSON wczytany pomyślnie.")
    elif input_file.lower().endswith((".yml", ".yaml")):
        data = load_yaml(input_file)
        print("YAML wczytany pomyślnie.")
    else:
        print("Obsługiwane są tylko .json i .yml/.yaml w tej wersji.")
        sys.exit(1)

    # Zapis wyjścia
    if output_file.lower().endswith(".json"):
        save_json(data, output_file)
    elif output_file.lower().endswith((".yml", ".yaml")):
        save_yaml(data, output_file)
    else:
        print("Format wyjściowy nie jest .json ani .yml/.yaml; wkrótce dodamy XML.")
        sys.exit(1)




if __name__ == "__main__":
    main()
