from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    test_priority_queueing_enqueue()
    test_priority_queueing_dequeue()
    test_priority_queueing_search()


def test_priority_queueing_enqueue():
    pq = PriorityQueue()
    pq.enqueue({
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["linha1", "linha2", "linha3"],
    })
    pq.enqueue({
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 7,
        "linhas_do_arquivo": [
            "linha1",
            "linha2",
            "linha3",
            "linha4",
            "linha5",
            "linha6",
            "linha7"],
    })
    pq.enqueue({"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 2,
               "linhas_do_arquivo": ["linha1", "linha2"]})

    assert len(pq) == 3
    assert len(pq.high_priority) == 2
    assert len(pq.regular_priority) == 1


def test_priority_queueing_dequeue():
    pq = PriorityQueue()
    pq.enqueue({"nome_do_arquivo": "arquivo1.txt", "qtd_linhas": 3,
               "linhas_do_arquivo": ["linha1", "linha2", "linha3"]})
    pq.enqueue({
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 7,
        "linhas_do_arquivo": [
               "linha1",
               "linha2",
               "linha3",
               "linha4",
               "linha5",
               "linha6",
               "linha7"],
    })
    pq.enqueue({"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 2,
               "linhas_do_arquivo": ["linha1", "linha2"]})

    assert len(pq) == 3
    assert pq.dequeue() == {
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 7,
        "linhas_do_arquivo": [
            "linha1",
            "linha2",
            "linha3",
            "linha4",
            "linha5",
            "linha6",
            "linha7"],
    }
    assert pq.dequeue() == {
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["linha1", "linha2", "linha3"]
    }
    assert pq.dequeue() == {"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 2,
                            "linhas_do_arquivo": ["linha1", "linha2"]}
    assert len(pq) == 0


def test_priority_queueing_search():
    pq = PriorityQueue()
    pq.enqueue({"nome_do_arquivo": "arquivo1.txt", "qtd_linhas": 3,
               "linhas_do_arquivo": ["linha1", "linha2", "linha3"]})
    pq.enqueue({
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 7,
        "linhas_do_arquivo": [
               "linha1",
               "linha2",
               "linha3",
               "linha4",
               "linha5",
               "linha6",
               "linha7"],
    })
    pq.enqueue({"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 2,
               "linhas_do_arquivo": ["linha1", "linha2"]})

    file1 = pq.search(0)
    file2 = pq.search(1)
    file3 = pq.search(2)

    assert file1["nome_do_arquivo"] == "arquivo3.txt"
    assert file2["nome_do_arquivo"] == "arquivo1.txt"
    assert file3["nome_do_arquivo"] == "arquivo2.txt"
