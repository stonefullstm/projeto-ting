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
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        path_file = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        sys.stdout.write(str(file))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
