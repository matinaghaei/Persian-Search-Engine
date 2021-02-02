import wikipedia


def mine_wikipedia():

    wikipedia.set_lang("fa")

    physics_cluster = wikipedia.search("فیزیک", results=55)
    for article in physics_cluster:
        text, title = handle_summary(article)
        write_text("Physics", title, text)

    math_cluster = wikipedia.search("ریاضیات", results=55)
    for article in math_cluster:
        text, title = handle_summary(article)
        write_text("Mathematics", title, text)

    health_cluster = wikipedia.search("سلامتی", results=55)
    for article in health_cluster:
        text, title = handle_summary(article)
        write_text("Health", title, text)

    history_cluster = wikipedia.search("تاریخ", results=55)
    for article in history_cluster:
        text, title = handle_summary(article)
        write_text("History", title, text)

    tech_cluster = wikipedia.search("تکنولوژی", results=55)
    for article in tech_cluster:
        text, title = handle_summary(article)
        write_text("Technology", title, text)


def write_text(subject, title, text):
    if text:
        file = open(f"Wikipedia Clusters/{subject}/{title}.txt", mode="w", encoding="utf-8")
        file.write(text)
        file.close()
        print(title)


def handle_summary(title):
    try:
        text = wikipedia.summary(title)
    except wikipedia.DisambiguationError as e:
        text, title = handle_disambiguation(e.options)
    return text, title


def handle_disambiguation(options):
    for title in options:
        try:
            text = wikipedia.summary(title)
        except wikipedia.DisambiguationError as e:
            pass
        else:
            return text, title
    return "", ""


if __name__ == '__main__':
    mine_wikipedia()
