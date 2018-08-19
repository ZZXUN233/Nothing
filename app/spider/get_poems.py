from app.spider.spiders import Spider


def make_search_api():
    search_url = "http://s.chinapoesy.com/?k="
    poem_name = "春的临终"
    poem_name = poem_name.lower().replace(" ", "")
    return search_url + poem_name


def get_content():
    key = make_search_api()
    print(key)
    spider = Spider("现代诗爬虫", key)
    b_soup = spider.get_soup()
    print(spider)
    temp = b_soup.find_all(id="content_lblSpeed")
    print(temp)


if __name__ == '__main__':
    get_content()
