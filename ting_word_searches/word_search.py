def exists_word(word, instance):
    word_in_files = []
    for index in range(len(instance)):
        file = instance.search(index)
        lines = []
        line = 0
        for file_line in file["linhas_do_arquivo"]:
            line += 1
            if word.lower() in file_line.lower():
                lines.append({"linha": line})
        if lines:
            word_in_files.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": lines
            })
    return word_in_files


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
