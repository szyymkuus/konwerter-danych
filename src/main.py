import sys
import os
import json
import yaml
from lxml import etree
import xml.etree.ElementTree as ET

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

def load_xml(path):
    """
    Wczytuje dane z pliku XML i weryfikuje, czy jest poprawnie sformatowany.
    Zwraca drzewo ElementTree
    """
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Błąd składni XML w pliku '{path}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Błąd odczytu pliku XML: {e}")
        sys.exit(1)

def dict_to_etree(data):
    root_name = next(iter(data))
    root_elem = ET.Element(root_name)

    for key, value in data[root_name].items():
        child = ET.SubElement(root_elem, key)
        child.text = str(value)

    return root_elem


def save_xml(data, path):
    try:
        if isinstance(data, ET.Element):
            tree = ET.ElementTree(data)
        else:
            root = dict_to_etree(data)
            tree = ET.ElementTree(root)

        # Zapis z deklaracją XML i kodowaniem UTF-8
        tree.write(path, encoding='utf-8', xml_declaration=True)
        print(f"Dane zapisano do XML w '{path}'.")
    except Exception as e:
        print(f"Błąd zapisu pliku XML: {e}")
        sys.exit(1)

def main():
    input_file, output_file = parse_args()

    if input_file.lower().endswith(".json"):
        data = load_json(input_file)
        print("JSON wczytany pomyślnie.")
    elif input_file.lower().endswith((".yml", ".yaml")):
        data = load_yaml(input_file)
        print("YAML wczytany pomyślnie.")
    elif input_file.lower().endswith(".xml"):
        data = load_xml(input_file)
        print("XML wczytany pomyślnie.")
    else:
        print("Obsługiwane są .json, .yml/.yaml oraz .xml w tej wersji.")
        sys.exit(1)


    # Zapis wyjścia
    if output_file.lower().endswith(".json"):
        save_json(data, output_file)
    elif output_file.lower().endswith((".yml", ".yaml")):
        save_yaml(data, output_file)
    elif output_file.lower().endswith(".xml"):
        save_xml(data, output_file)
    else:
        print("Obsługiwane formaty wyjścia: .json, .yml/.yaml, .xml")
        sys.exit(1)




if __name__ == "__main__":
    main()
