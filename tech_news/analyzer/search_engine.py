from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    title_search = search_news({"title": {"$regex": f"{title.lower()}"}})

    news = [(news["title"], news["url"]) for news in title_search]

    return news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        if not bool(datetime.strptime(date, "%Y-%m-%d")):
            raise ValueError

        date_search = search_news({
            "timestamp":  "/".join(reversed(date.split('-')))})

        news = [(news["title"], news["url"]) for news in date_search]

        return news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    tag_search = search_news({"tags": {
        "$regex": f"{tag.lower().capitalize()}"}})
    news = [(news["title"], news["url"]) for news in tag_search]

    return news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
