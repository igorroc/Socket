def get_base():
    import utils.dataset.tweets500 as tweets
    return tweets.BASE


'''
def get_base():
    import utils.dataset.books_pt as books_pt

    BASE = []
    for book in books_pt.books_neg:
        BASE.append((book, 'negativo'))

    for book in books_pt.books_pos:
        BASE.append((book, 'positivo'))

    return BASE
'''
