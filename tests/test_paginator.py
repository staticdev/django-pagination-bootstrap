from django.core.paginator import Paginator
from django.test import TestCase

from django_pagination_bootstrap import paginator
from django_pagination_bootstrap.templatetags import pagination_tags


class TestPaginator(TestCase):
    def test_page_obj_one(self) -> None:
        p = Paginator(range(15), 2)
        pg = pagination_tags.paginate({"paginator": p, "page_obj": p.page(1)})
        self.assertEqual(pg["pages"], [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(pg["records"]["first"], 1)
        self.assertEqual(pg["records"]["last"], 2)

    def test_page_obj_eight(self) -> None:
        p = Paginator(range(15), 2)
        pg = pagination_tags.paginate({"paginator": p, "page_obj": p.page(8)})
        self.assertEqual(pg["pages"], [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(pg["records"]["first"], 15)
        self.assertEqual(pg["records"]["last"], 15)

    def test_pages_list(self) -> None:
        p = Paginator(range(17), 2)
        pages = pagination_tags.paginate({"paginator": p, "page_obj": p.page(1)})[
            "pages"
        ]
        self.assertEqual(pages, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_truncated_pages_list(self) -> None:
        p = Paginator(range(19), 2)
        pages = pagination_tags.paginate({"paginator": p, "page_obj": p.page(1)})[
            "pages"
        ]
        self.assertEqual(pages, [1, 2, 3, 4, None, 7, 8, 9, 10])

    def test_longer_truncated_pages_list(self) -> None:
        p = Paginator(range(21), 2)
        pages = pagination_tags.paginate({"paginator": p, "page_obj": p.page(1)})[
            "pages"
        ]
        self.assertEqual(pages, [1, 2, 3, 4, None, 8, 9, 10, 11])

    def test_orphaned_page_list(self) -> None:
        p = Paginator(range(5), 2, 1)
        pages = pagination_tags.paginate({"paginator": p, "page_obj": p.page(1)})[
            "pages"
        ]
        self.assertEqual(pages, [1, 2])

    def test_orphaned_page_obj_one(self) -> None:
        p = Paginator(range(5), 2, 1)
        pg = pagination_tags.paginate({"paginator": p, "page_obj": p.page(1)})
        self.assertTrue(pg["pages"], [1, 2, 3, 4, None, 7, 8, 9, 10])
        self.assertTrue(pg["records"]["first"], 1)
        self.assertTrue(pg["records"]["last"], 2)

    def test_orphaned_page_obj_ten(self) -> None:
        p = Paginator(range(21), 2, 1)
        pg = pagination_tags.paginate({"paginator": p, "page_obj": p.page(10)})
        self.assertTrue(pg["pages"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertTrue(pg["records"]["first"], 19)
        self.assertTrue(pg["records"]["last"], 21)


class TestInfinitePaginator(TestCase):
    def test_paginate_range_by_two(self) -> None:
        pg = paginator.InfinitePaginator(range(20), 2, link_template="/bacon/page/%d")
        self.assertEqual(pg.validate_number(2), 2)
        self.assertEqual(pg.orphans, 0)
        p3 = pg.page(3)
        self.assertIsInstance(p3, paginator.InfinitePage)
        self.assertEqual(p3.end_index(), 6)
        self.assertTrue(p3.has_next())
        self.assertTrue(p3.has_previous())
        self.assertEqual(p3.next_link(), "/bacon/page/4")
        self.assertEqual(p3.previous_link(), "/bacon/page/2")
        p10 = pg.page(10)
        self.assertFalse(p10.has_next())
        self.assertTrue(p10.has_previous())


class TestFinitePaginator(TestCase):
    def test_paginate_range_by_two_offset_ten(self) -> None:
        pg = paginator.FinitePaginator(
            range(20), 2, offset=10, link_template="/bacon/page/%d"
        )
        self.assertEqual(pg.validate_number(2), 2)
        self.assertEqual(pg.orphans, 0)
        p3 = pg.page(3)
        self.assertIsInstance(p3, paginator.FinitePage)
        self.assertEqual(p3.start_index(), 10)
        self.assertEqual(p3.end_index(), 6)
        self.assertTrue(p3.has_next())
        self.assertTrue(p3.has_previous())
        self.assertEqual(p3.next_link(), "/bacon/page/4")
        self.assertEqual(p3.previous_link(), "/bacon/page/2")

    def test_paginate_range_by_twenty_offset_ten(self) -> None:
        pg = paginator.FinitePaginator(
            range(20), 20, offset=10, link_template="/bacon/page/%d"
        )
        self.assertEqual(pg.validate_number(2), 2)
        self.assertEqual(pg.orphans, 0)
        p2 = pg.page(2)
        self.assertIsInstance(p2, paginator.FinitePage)
        self.assertEqual(p2.start_index(), 10)
        self.assertEqual(p2.end_index(), 40)
        self.assertFalse(p2.has_next())
        self.assertTrue(p2.has_previous())
        self.assertIsNone(p2.next_link())
        self.assertEqual(p2.previous_link(), "/bacon/page/1")
