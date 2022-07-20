# Requisito 1
import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        request = requests.get(url, timeout=3)
        if request.status_code == 200:
            return request.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css(".cs-overlay-link::attr(href)").getall()

    return url


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css("a.next::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news_dict = dict()
    news_dict['url'] = selector.css("link[rel=canonical]::attr(href)").get()
    news_dict['title'] = selector.css(".entry-title::text").get()
    news_dict['timestamp'] = selector.css(".meta-date::text").get()
    news_dict['writer'] = selector.css(".author a::text").get()
    news_dict['comments_count'] = len(
        selector.css(".comment-list li").getall())
    news_dict['summary'] = "".join(
        selector.css(".entry-content p:nth-child(2) *::text").getall())
    news_dict['tags'] = selector.css(".post-tags a::text").getall()
    news_dict['category'] = selector.css(".label::text").get()

    return news_dict


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
