import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_lines = txt_importer(path_file)
    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines
    }
    index = 0
    while (index < len(instance)
           and instance.search(index)["nome_do_arquivo"] != path_file):
        index += 1
    if index >= len(instance):
        instance.enqueue(file_dict)
        sys.stdout.write(str(file_dict))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
