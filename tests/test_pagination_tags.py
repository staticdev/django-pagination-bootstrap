from django import template
from django.test import TestCase

from .test_http_request import TestHttpRequest


class TestTemplatePaginateTags(TestCase):
    def test_render_range_by_two(self) -> None:
        t = template.Template(
            "{% load pagination_tags %}{% autopaginate var 2 %}{% paginate %}"
        )
        c = template.Context({"var": range(21), "request": TestHttpRequest()})
        self.assertEqual(
            t.render(c),
            '\n\n\n<nav aria-label="Page pagination">\n  <ul class="pagination">\n  \n    <li class="page-item disabled"><a class="page-link" href="#" onclick="javascript: return false;">&laquo;</a></li>\n  \n  \n    \n      \n    <li class="page-item active"><a class="page-link" href="#" onclick="javascript: return false;">1</a></li>\n      \n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=2">2</a></li>\n      \n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=3">3</a></li>\n      \n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=4">4</a></li>\n      \n    \n  \n    \n    <li class="page-item disabled"><a class="page-link" href="#" onclick="javascript: return false;">...</a></li>\n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=8">8</a></li>\n      \n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=9">9</a></li>\n      \n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=10">10</a></li>\n      \n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=11">11</a></li>\n      \n    \n  \n  \n    <li class="page-item"><a class="page-link" href="?page=2">&raquo;</a></li>\n  \n  </ul>\n  \n</nav>\n',
        )

    def test_render_range_by_two_one_orphan(self) -> None:
        t = template.Template(
            "{% load pagination_tags %}{% autopaginate var 2 1 %}{% paginate %}"
        )
        c = template.Context({"var": range(20), "request": TestHttpRequest()})
        self.assertEqual(
            t.render(c),
            '\n\n\n<nav aria-label="Page pagination">\n  <ul class="pagination">\n  \n    <li class="page-item disabled"><a class="page-link" href="#" onclick="javascript: return false;">&laquo;</a></li>\n  \n  \n    \n      \n    <li class="page-item active"><a class="page-link" href="#" onclick="javascript: return false;">1</a></li>\n      \n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=2">2</a></li>\n      \n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=3">3</a></li>\n      \n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=4">4</a></li>\n      \n    \n  \n    \n    <li class="page-item disabled"><a class="page-link" href="#" onclick="javascript: return false;">...</a></li>\n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=7">7</a></li>\n      \n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=8">8</a></li>\n      \n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=9">9</a></li>\n      \n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=10">10</a></li>\n      \n    \n  \n  \n    <li class="page-item"><a class="page-link" href="?page=2">&raquo;</a></li>\n  \n  </ul>\n  \n</nav>\n',
        )

    def test_render_range_by_one(self) -> None:
        t = template.Template(
            "{% load pagination_tags %}{% autopaginate var %}{% paginate %}"
        )
        c = template.Context({"var": range(21), "request": TestHttpRequest()})
        self.assertEqual(
            t.render(c),
            '\n\n\n<nav aria-label="Page pagination">\n  <ul class="pagination">\n  \n    <li class="page-item disabled"><a class="page-link" href="#" onclick="javascript: return false;">&laquo;</a></li>\n  \n  \n    \n      \n    <li class="page-item active"><a class="page-link" href="#" onclick="javascript: return false;">1</a></li>\n      \n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=2">2</a></li>\n      \n    \n  \n  \n    <li class="page-item"><a class="page-link" href="?page=2">&raquo;</a></li>\n  \n  </ul>\n  \n</nav>\n',
        )

    def test_render_range_by_twenty(self) -> None:
        t = template.Template(
            "{% load pagination_tags %}{% autopaginate var 20 %}{% paginate %}"
        )
        c = template.Context({"var": range(21), "request": TestHttpRequest()})
        self.assertEqual(
            t.render(c),
            '\n\n\n<nav aria-label="Page pagination">\n  <ul class="pagination">\n  \n    <li class="page-item disabled"><a class="page-link" href="#" onclick="javascript: return false;">&laquo;</a></li>\n  \n  \n    \n      \n    <li class="page-item active"><a class="page-link" href="#" onclick="javascript: return false;">1</a></li>\n      \n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=2">2</a></li>\n      \n    \n  \n  \n    <li class="page-item"><a class="page-link" href="?page=2">&raquo;</a></li>\n  \n  </ul>\n  \n</nav>\n',
        )

    def test_render_range_by_var(self) -> None:
        t = template.Template(
            "{% load pagination_tags %}{% autopaginate var by %}{% paginate %}"
        )
        c = template.Context({"var": range(21), "by": 20, "request": TestHttpRequest()})
        self.assertEqual(
            t.render(c),
            '\n\n\n<nav aria-label="Page pagination">\n  <ul class="pagination">\n  \n    <li class="page-item disabled"><a class="page-link" href="#" onclick="javascript: return false;">&laquo;</a></li>\n  \n  \n    \n      \n    <li class="page-item active"><a class="page-link" href="#" onclick="javascript: return false;">1</a></li>\n      \n    \n  \n    \n      \n    <li class="page-item"><a class="page-link" href="?page=2">2</a></li>\n      \n    \n  \n  \n    <li class="page-item"><a class="page-link" href="?page=2">&raquo;</a></li>\n  \n  </ul>\n  \n</nav>\n',
        )

    def test_render_range_by_var_as_name(self) -> None:
        t = template.Template(
            "{% load pagination_tags %}{% autopaginate var by as foo %}{{ foo }}"
        )
        c = template.Context(
            {"var": list(range(21)), "by": 20, "request": TestHttpRequest()}
        )
        self.assertEqual(
            t.render(c),
            "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]",
        )

    def test_render_invalid_arguments(self) -> None:
        with self.assertRaisesMessage(
            template.TemplateSyntaxError,
            "autopaginate tag takes one required argument and one optional argument",
        ):
            template.Template("{% load pagination_tags %}{% autopaginate %}")

    def test_render_invalid_orphans(self) -> None:
        with self.assertRaisesMessage(
            template.TemplateSyntaxError, "Got a, but expected integer."
        ):
            template.Template("{% load pagination_tags %}{% autopaginate var 2 a %}")

    def test_render_range_by_var_as_index_error(self) -> None:
        with self.assertRaisesMessage(
            template.TemplateSyntaxError,
            "Context variable assignment must take the form of {% autopaginate object.example_set.all ... as context_var_name %}",
        ):
            template.Template("{% load pagination_tags %}{% autopaginate var by as %}")
