from bs4 import BeautifulSoup

class Related:
    def __init__(self, html):
        self._html = html
        self._soup = BeautifulSoup(self._html, 'html.parser')
        self._ids = []

    @property
    def related_ids(self):
        if len(self._ids):
            return self._ids

        ids = []
        container = self._soup.find(id='bootstrap-overrides')
        if container:
            divs = container.find_all('div')
            for el in divs:
                href = el.get('href')
                if href:
                    id = href.split('/')[2]
                    ids.append(id)

        self._ids = ids
        return ids

    @property
    def number_of_listings(self):
        return len(self.related_ids)
