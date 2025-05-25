class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        if not isinstance(name,str):
            raise Exception("Name must be a string")
        if len(name.strip()) == 0:
            raise Exception("Name must be longer that 0 characters")
        self.name = name

        @property
        def name(self):
            return self._name
        

    def articles(self):
         return [article for article in Article.all if article.author == self]


    def magazines(self):
       return list({article.magazine for article in self.articles()})


    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({article.magazine.category for article in self.articles()})

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass