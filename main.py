import os
from documents import Documents
from tokenizer import Tokenizer
from indexer import Indexer
from query_processor import QueryProcessor


def main():
    docs = Documents()
    read_files("sampleDoc/", docs)
    tokenizer = Tokenizer(docs)
    indexer = Indexer(tokenizer.positionals, docs, stopwords_threshold=30, champion_list_size=10)
    query_processor = QueryProcessor(indexer.inverted_index, docs)

    running = True
    while running:
        query = input("Enter your query (Or type 'terminate'): ")
        if query == 'terminate':
            running = False
        else:
            results = query_processor.search(query, top=5)
            print()
            if len(results) == 0:
                print("No Results :(")
            for i in range(len(results)):
                print("{index}. Doc{doc_id} \t\t -- \t\t Cosine Score : {similarity}"
                      .format(index=i + 1, doc_id=results[i][0], similarity=results[i][1]))
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
