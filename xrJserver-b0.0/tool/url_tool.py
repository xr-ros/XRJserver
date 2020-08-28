from xrJserver.base_class.url import url


def include(p_url, sub_urls):
    urls = None

    for old_url_tab in sub_urls:
        for old_url in old_url_tab.get_url_tab():

            path, fun = old_url
            path = p_url + path

            if not urls:
                urls = url(path, fun)
            else:
                urls.insert_url(path, fun)

    return urls
