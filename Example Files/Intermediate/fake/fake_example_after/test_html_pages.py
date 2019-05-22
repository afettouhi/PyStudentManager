import unittest
import os
import tempfile
import io

from html_pages import HtmlPagesConverter, FileAccessWrapper


class HtmlPagesTest(unittest.TestCase):
    def test_returns_unconverted_first_html_page(self):
        filename = os.path.join(tempfile.gettempdir(), "afile.txt")
        f = open(filename, "w", encoding="UTF-8")
        f.write("plain text\n")
        f.close()
        converter = HtmlPagesConverter(FileAccessWrapper(filename))
        first_page = converter.get_html_page(0)
        self.assertEqual("plain text\n", first_page)

    def test_inserts_br_tags_for_linebreaks(self):
        filename = os.path.join(tempfile.gettempdir(), "afile.txt")
        f = open(filename, "w", encoding="UTF-8")
        f.write("plain text\n")
        f.close()
        converter = HtmlPagesConverter(FileAccessWrapper(filename))
        get_text = converter.get_html_page(0)
        new_text = converter.convert_html_page(get_text)
        self.assertEqual("plain text<br />", new_text)
        
    def test_quotes_escaped(self):
        converter = HtmlPagesConverter(FakeFileWrapper("text with 'quotes'"))
        get_text = converter.get_html_page(0)
        new_text = converter.convert_html_page(get_text)
        self.assertEqual("text with &#x27;quotes&#x27;<br />", new_text)

    def test_random_access_pages(self):
        converter = HtmlPagesConverter(FakeFileWrapper("page one\nPAGE_BREAK\npage two"))
        page_two = converter.get_html_page(1)
        self.assertEqual("page two", page_two)

    def test_random_access_pages_quoted(self):
        converter = HtmlPagesConverter(FakeFileWrapper("page one\nPAGE_BREAK\npage two\nPAGE_BREAK\npage three"))
        page_two = converter.get_html_page(1)
        converted_page_two = converter.convert_html_page(page_two)
        self.assertEqual("page two<br />", converted_page_two)
         
        
class FakeFileWrapper:
    def __init__(self, text):
        self.text = text
        
    def open(self):
        return io.StringIO(self.text)
