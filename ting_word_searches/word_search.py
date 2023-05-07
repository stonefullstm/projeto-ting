def search_word(word, instance, content=False):
    word_in_files = []
    for index in range(len(instance)):
        file = instance.search(index)
        lines = []
        for line, file_line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in file_line.lower():
                line_dict = (
                    {"linha": line + 1, "conteudo": file_line}
                    if content else {"linha": line + 1}
                            )
                lines.append(line_dict)
        if lines:
            word_in_files.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": lines
            })
    return word_in_files


def exists_word(word, instance):
    return search_word(word, instance)


def search_by_word(word, instance):
    return search_word(word, instance, True)
