import os
from documents import Documents
from tokenizer import Tokenizer
from indexer import Indexer
from query_processor import QueryProcessor


def main():
    docs = Documents()
    read_files("sampleDoc/", docs)
    tokenizer = Tokenizer(docs)
    indexer = Indexer(tokenizer.positionals, docs, 30, 5)
    query_processor = QueryProcessor(indexer.inverted_index)

    running = True
    while running:
        query = input("Enter your query (Or type 'terminate'): ")
        if query == 'terminate':
            running = False
        else:
            results = query_processor.search(query)
            for i in range(len(results)):
                print("{index}. Doc{doc_id} - Contains {word_count} word(s)"
                      .format(index=i, doc_id=results[i][0], word_count=results[i][1]))
            print()


def read_files(directory, docs):
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            f = open(os.path.join(directory, file), mode="r", encoding="utf-8")
            entire_text = f.read()
            f.close()
            docs.add(int(file.replace('.txt', '')), entire_text)


if __name__ == '__main__':
    main()
