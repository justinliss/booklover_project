from booklover import BookLover
import unittest
import pandas as pd

class BookLoverTestSuite(unittest.TestCase): 

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        booklover1 = BookLover("Justin","justin@gmail.com","comedy")
        booklover1.add_book("comedy book", 4)
        self.assertTrue("comedy book" in set(booklover1.book_list["book_name"]))
    
    def test_2_add_book(self): 
        # add the same book twice. Test if it's in `book_list` only once.
        booklover1 = BookLover("Justin","justin@gmail.com","comedy")
        booklover1.add_book("comedy book", 4)
        booklover1.add_book("comedy book", 4)
        
        expected = 1
        #self.assertEqual(len(booklover1.book_list[booklover1.book_list["book_name"]=="comedy_book"]), expected)
        self.assertEqual(booklover1.num_books,expected)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        booklover1 = BookLover("Justin",
                               "justin@gmail.com",
                               "comedy", 
                               1, 
                               pd.DataFrame({'book_name':["comedy book"], 'book_rating':[4]}) )
        
        self.assertTrue(booklover1.has_read("comedy book"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        booklover1 = BookLover("Justin",
                               "justin@gmail.com",
                               "comedy", 
                               1, 
                               pd.DataFrame({'book_name':["comedy book"], 'book_rating':[4]}) )
        
        self.assertFalse(booklover1.has_read("horror book"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        booklover1 = BookLover("Justin",
                               "justin@gmail.com",
                               "comedy", 
                               1, 
                               pd.DataFrame({'book_name':["comedy book"], 'book_rating':[4]}) )
        booklover1.add_book("horror book", 5)
        booklover1.add_book("drama book", 6)
        
        expected = 3
        self.assertEqual(booklover1.num_books_read(), expected)
        
    def test_6_fav_books(self): 
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        booklover1 = BookLover("Justin",
                               "justin@gmail.com",
                               "comedy", 
                               1, 
                               pd.DataFrame({'book_name':["comedy book"], 'book_rating':[1]}) )
        booklover1.add_book("horror book", 5)
        booklover1.add_book("drama book", 6)
        
        self.assertTrue(booklover1.fav_books()["book_rating"].min() >= 3)

if __name__ == '__main__':
    unittest.main(verbosity=3)