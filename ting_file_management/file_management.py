import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            raise TypeError
        file = open(path_file, mode="r")
        return [line.rstrip("\n") for line in file]
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    except TypeError:
        sys.stderr.write("Formato inválido")
