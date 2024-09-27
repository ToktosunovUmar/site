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
                              verbose_name='enter title book', db_index=True, null=True)
    author = models.CharField(max_length=255,
                              verbose_name='author name', db_index=True, null=True)
    image = models.ImageField(upload_to='post/',
                              verbose_name='download picture', db_index=True, null=True)
    pages = models.IntegerField(verbose_name='number of pages', db_index=True, null=True)
    summary = models.TextField(verbose_name='write description', db_index=True, null=True)
    url = models.URLField(verbose_name='write url of  news', db_index=True, null=True)
    email = models.EmailField(verbose_name='write your email', db_index=True, null=True)
    genre = models.CharField(max_length=100, choices=GENRE, db_index=True, null=True)

    publication_date = models.DateTimeField(auto_now_add=True, db_index=True, null=True)

    def __str__(self):
        return f'{self.tittle} - {self.image}'


class Reviewbook(models.Model):
    book_review = models.ForeignKey(books_post, on_delete=models.CASCADE,
                                    related_name='review_book', db_index=True, null=True)
    text_book = models.TextField(db_index=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True)

    def __str__(self):
        return f'{self.text_book} - {self.created_at}'
