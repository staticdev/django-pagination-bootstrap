try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.template import Template, Context
from django.test import TestCase

from .middleware import PaginationMiddleware
from .paginator import (
    InfinitePaginator,
    InfinitePage,
    FinitePaginator,
    FinitePage,
)
from .templatetags.pagination_tags import paginate


class TestPaginator(TestCase):

    def test_page_obj_one(self):
        p = Paginator(range(15), 2)
        pg = paginate({'paginator': p, 'page_obj': p.page(1)})
        self.assertEqual(pg['pages'], [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(pg['records']['first'], 1)
        self.assertEqual(pg['records']['last'], 2)

    def test_page_obj_eight(self):
        p = Paginator(range(15), 2)
        pg = paginate({'paginator': p, 'page_obj': p.page(8)})
        self.assertEqual(pg['pages'], [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(pg['records']['first'], 15)
        self.assertEqual(pg['records']['last'], 15)

    def test_pages_list(self):
        p = Paginator(range(17), 2)
        pages = paginate({'paginator': p, 'page_obj': p.page(1)})['pages']
        self.assertEqual(pages, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_truncated_pages_list(self):
        p = Paginator(range(19), 2)
        pages = paginate({'paginator': p, 'page_obj': p.page(1)})['pages']
        self.assertEqual(pages, [1, 2, 3, 4, None, 7, 8, 9, 10])

    def test_longer_truncated_pages_list(self):
        p = Paginator(range(21), 2)
        pages = paginate({'paginator': p, 'page_obj': p.page(1)})['pages']
        self.assertEqual(pages, [1, 2, 3, 4, None, 8, 9, 10, 11])

    def test_orphaned_page_list(self):
        p = Paginator(range(5), 2, 1)
        pages = paginate({'paginator': p, 'page_obj': p.page(1)})['pages']
        self.assertEqual(pages, [1, 2])

    def test_orphaned_page_obj_one(self):
        p = Paginator(range(5), 2, 1)
        pg = paginate({'paginator': p, 'page_obj': p.page(1)})
        self.assertTrue(pg['pages'], [1, 2, 3, 4, None, 7, 8, 9, 10])
        self.assertTrue(pg['records']['first'], 1)
        self.assertTrue(pg['records']['last'], 2)

    def test_orphaned_page_obj_ten(self):
        p = Paginator(range(21), 2, 1)
        pg = paginate({'paginator': p, 'page_obj': p.page(10)})
        self.assertTrue(pg['pages'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertTrue(pg['records']['first'], 19)
        self.assertTrue(pg['records']['last'], 21)


from django.http import HttpRequest as DjangoHttpRequest


class TestHttpRequest(DjangoHttpRequest):
    page = 1


class TestTemplatePaginateTags(TestCase):

    def test_render_range_by_two(self):
        t = Template("{% load pagination_tags %}{% autopaginate var 2 %}{% paginate %}")
        c = Context({'var': range(21), 'request': TestHttpRequest()})
        self.assertEqual(t.render(c), u'\n\n\n<ul class="pagination">\n\n  <li class="disabled"><a href="#" onclick="javascript: return false;">&laquo;</a></li>\n\n\n  \n    \n  <li class="active"><a href="#" onclick="javascript: return false;">1</a></li>\n    \n  \n\n  \n    \n  <li><a href="?page=2">2</a></li>\n    \n  \n\n  \n    \n  <li><a href="?page=3">3</a></li>\n    \n  \n\n  \n    \n  <li><a href="?page=4">4</a></li>\n    \n  \n\n  \n  <li class="disabled"><a href="#" onclick="javascript: return false;">...</a></li>\n  \n\n  \n    \n  <li><a href="?page=8">8</a></li>\n    \n  \n\n  \n    \n  <li><a href="?page=9">9</a></li>\n    \n  \n\n  \n    \n  <li><a href="?page=10">10</a></li>\n    \n  \n\n  \n    \n  <li><a href="?page=11">11</a></li>\n    \n  \n\n\n  <li><a href="?page=2">&raquo;</a></li>\n\n</ul>\n\n')

    def test_render_range_by_one(self):
        t = Template("{% load pagination_tags %}{% autopaginate var %}{% paginate %}")
        c = Context({'var': range(21), 'request': TestHttpRequest()})
        self.assertEqual(t.render(c), u'\n\n\n<ul class="pagination">\n\n  <li class="disabled"><a href="#" onclick="javascript: return false;">&laquo;</a></li>\n\n\n  \n    \n  <li class="active"><a href="#" onclick="javascript: return false;">1</a></li>\n    \n  \n\n  \n    \n  <li><a href="?page=2">2</a></li>\n    \n  \n\n\n  <li><a href="?page=2">&raquo;</a></li>\n\n</ul>\n\n')

    def test_render_range_by_twenty(self):
        t = Template("{% load pagination_tags %}{% autopaginate var 20 %}{% paginate %}")
        c = Context({'var': range(21), 'request': TestHttpRequest()})
        self.assertEqual(t.render(c), u'\n\n\n<ul class="pagination">\n\n  <li class="disabled"><a href="#" onclick="javascript: return false;">&laquo;</a></li>\n\n\n  \n    \n  <li class="active"><a href="#" onclick="javascript: return false;">1</a></li>\n    \n  \n\n  \n    \n  <li><a href="?page=2">2</a></li>\n    \n  \n\n\n  <li><a href="?page=2">&raquo;</a></li>\n\n</ul>\n\n')

    def test_render_range_by_var(self):
        t = Template("{% load pagination_tags %}{% autopaginate var by %}{% paginate %}")
        c = Context({'var': range(21), 'by': 20, 'request': TestHttpRequest()})
        self.assertEqual(t.render(c), u'\n\n\n<ul class="pagination">\n\n  <li class="disabled"><a href="#" onclick="javascript: return false;">&laquo;</a></li>\n\n\n  \n    \n  <li class="active"><a href="#" onclick="javascript: return false;">1</a></li>\n    \n  \n\n  \n    \n  <li><a href="?page=2">2</a></li>\n    \n  \n\n\n  <li><a href="?page=2">&raquo;</a></li>\n\n</ul>\n\n')

    def test_render_range_by_var_as_name(self):
        t = Template("{% load pagination_tags %}{% autopaginate var by as foo %}{{ foo }}")
        c = Context({'var': list(range(21)), 'by': 20, 'request': TestHttpRequest()})
        self.assertEqual(t.render(c), u'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]')


class TestInfinitePaginator(TestCase):

    def test_paginate_range_by_two(self):
        pg = InfinitePaginator(range(20), 2, link_template='/bacon/page/%d')
        self.assertEqual(pg.validate_number(2), 2)
        self.assertEqual(pg.orphans, 0)
        p3 = pg.page(3)
        self.assertIsInstance(p3, InfinitePage)
        self.assertEqual(p3.end_index(), 6)
        self.assertTrue(p3.has_next())
        self.assertTrue(p3.has_previous())
        self.assertEqual(p3.next_link(), '/bacon/page/4')
        self.assertEqual(p3.previous_link(), '/bacon/page/2')
        p10 = pg.page(10)
        self.assertFalse(p10.has_next())
        self.assertTrue(p10.has_previous())


class TestFinitePaginator(TestCase):

    def test_paginate_range_by_two_offset_ten(self):
        pg = FinitePaginator(range(20), 2, offset=10, link_template='/bacon/page/%d')
        self.assertEqual(pg.validate_number(2), 2)
        self.assertEqual(pg.orphans, 0)
        p3 = pg.page(3)
        self.assertIsInstance(p3, FinitePage)
        self.assertEqual(p3.start_index(), 10)
        self.assertEqual(p3.end_index(), 6)
        self.assertTrue(p3.has_next())
        self.assertTrue(p3.has_previous())
        self.assertEqual(p3.next_link(), '/bacon/page/4')
        self.assertEqual(p3.previous_link(), '/bacon/page/2')

    def test_paginate_range_by_twenty_offset_ten(self):
        pg = FinitePaginator(range(20), 20, offset=10, link_template='/bacon/page/%d')
        self.assertEqual(pg.validate_number(2), 2)
        self.assertEqual(pg.orphans, 0)
        p2 = pg.page(2)
        self.assertIsInstance(p2, FinitePage)
        self.assertEqual(p2.start_index(), 10)
        self.assertEqual(p2.end_index(), 40)
        self.assertFalse(p2.has_next())
        self.assertTrue(p2.has_previous())
        self.assertIsNone(p2.next_link())
        self.assertEqual(p2.previous_link(), '/bacon/page/1')


class TestPaginationMiddleware(TestCase):

    def test_append_page_property(self):
        middleware = PaginationMiddleware()
        request = WSGIRequest({'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': 'multipart', 'wsgi.input': StringIO()})
        middleware.process_request(request)
        self.assertTrue(hasattr(request, 'page'))
        request.upload_handlers.append('asdf')
