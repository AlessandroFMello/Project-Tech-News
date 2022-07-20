from tech_news.database import search_news
# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    title_search = search_news({"title": {"$regex": f"{title.lower()}"}})

    news = [(news["title"], news["url"]) for news in title_search]

    return news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
