class Article:
    all = []  #  This tracks all article instances

    def __init__(self, author, magazine, title):
        # validate title
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not 5 <= len(title) <= 50:
            raise Exception("Title must be between 5 and 50 characters")
        
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance")
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name.strip()) == 0:
            raise Exception("Name must be longer than 0 characters")
        self._name = name 

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
    all =[] #This tracks all the magazine instances
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be a string of 2 to 16 characters")
        if not isinstance(category, str) or len(category.strip()) == 0:
            raise Exception("Category must be a non-empty string")

        self.name = name
        self.category = category
        Magazine.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._category = value
        else:
            raise Exception("Category must be a non-empty string")


    def articles(self):
        return [article for article in Article.all if article.magazine == self]


    def contributors(self):
        return list({article.author for article in self.articles()})


    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        from collections import Counter
        author_count = Counter([article.author for article in self.articles()])
        authors = [author for author, count in author_count.items() if count > 2]
        return authors if authors else None