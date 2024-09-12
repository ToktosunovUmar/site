from django.db import models


class books_post(models.Model):
    GENRE = (
        [
         ('biography', 'Biography'),
         ('history', 'History'),
         ('mystery', 'Mystery'),
         ('fantasy', 'Fantasy'),
         ]
    )
    #
    tittle = models.CharField(max_length=255,
                              verbose_name='enter title book')
    author = models.CharField(max_length=255,
                              verbose_name='author name')
    image = models.ImageField(upload_to='post/',
                              verbose_name='download picture')
    pages = models.IntegerField(verbose_name='number of pages')
    summary = models.TextField(verbose_name='write description')
    url = models.URLField(verbose_name='write url of  news')
    email = models.EmailField(verbose_name='write your email')
    genre = models.CharField(max_length=100, choices=GENRE)

    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tittle} - {self.image}'


class Reviewbook(models.Model):
    book_review = models.ForeignKey(books_post, on_delete=models.CASCADE, related_name='review_book')
    text_book = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text_book} - {self.created_at}'
