#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from parameterized import parameterized
import client
import utils
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class
    inherit fro unittest.TestCase
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
        ])
    @patch("client.get_json")
    def test_org(self, org_n, mock_method):
        """test org

        Arguments
        ---------
        org_n: str
        mock_meck_method: Mock

        Return
        ------
        None
        """
        orgInstance = GithubOrgClient(org_n)
        orgInstance.org
        url = orgInstance.ORG_URL.format(org=org_n)
        mock_method.assert_called_once_with(url)

    def test_public_repos_url(self):
        """test public repos url"""
        pass


if __name__ == "__main__":
    unittest.main()
