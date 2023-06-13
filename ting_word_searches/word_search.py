def exists_word(word, instance):
    result = []
    for file in instance.queue:
        file_info = {"palavra": word,
                     "arquivo": file["nome_do_arquivo"], "ocorrencias": []}
        for i, line in enumerate(file["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                file_info["ocorrencias"].append({"linha": i})
        if file_info["ocorrencias"]:
            result.append(file_info)
    return result


def search_by_word(word, instance):
    return [
        {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": i+1, "conteudo": line.strip()}
                for i, line in enumerate(file["linhas_do_arquivo"])
                if word.lower() in line.lower()
            ]
        }
        for file in instance.queue
        if any(word.lower() in line.lower() for line
               in file["linhas_do_arquivo"])
    ]
