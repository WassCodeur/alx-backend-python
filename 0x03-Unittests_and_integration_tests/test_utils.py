#!/usr/bin/env python3
"""unit test"""

from parameterized import parameterized
from unittest.mock import patch
import requests
import unittest
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a"), KeyError),
        ({"a", 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        (
            (
                "http://example.com",
                {"payload": True}
            )
        ),
        (
            (
                "http://holberton.io",
                {"payload": False}
            )
        )
    ])
    def test_get_json(self, test_url, test_payload):
        return_value = {"return_value.json.return_value": test_payload}
        patcher = patch("requests.get", **return_value)
        mock = patcher.start()
        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        mock.assert_called_once()

        patcher.stop()


class TestMemoize(unittest.TestCase):

    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        patcher = patch.object(TestClass, "a_method")
        mock_test = patcher.start()

        newTestClass = TestClass()
        first_call_result = newTestClass.a_property()

        mock_test.assert_called_once()
        mock_test.reset_mock()

        newTestClass = TestClass()
        second_call_result = newTestClass.a_property()

        mock_test.assert_not_called()

        self.assertEqual(first_call_result, second_call_result)
        patcher.stop()


if __name__ == "__main__":
    unittest.main()
