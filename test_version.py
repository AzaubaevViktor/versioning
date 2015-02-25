from unittest import TestCase

from version_set import Version

__author__ = 'ktulhy'


class TestVersion(TestCase):
    def test_parse(self):
        version = Version()
        tests = {
            "v0.1-2-hash":      "0.1.2.hash",
            "0.1-2-hash":       "0.1.2.hash",
            "v0.1a-3-hash":     "0.1.3.hash[a]",
            "0.1a-3-hash":      "0.1.3.hash[a]",
            "12.1a-3-hash":     "12.1.3.hash[a]",
            "1.33a-3-hash":     "1.33.3.hash[a]",
            "1.3a-45-hashi":    "1.3.45.hashi[a]",
            "1.2pa-3-hash":     "1.2.3.hash[pa]",
            "1.2b-3-hash":      "1.2.3.hash[b]",
            "1.2rc-3-hash":     "1.2.3.hash[rc]",
            "1.2rc2-3-hash":    "1.2.3.hash[rc2]",
            "1.2rc34-3-hash":  "1.2.3.hash[rc34]",
            "1.2rtm-3-hash": "1.2.3.hash[rtm]",
            "1.2ga-3-hash":  "1.2.3.hash[ga]",
            "1.2eol-3-hash": "1.2.3.hash[eol]",
            "1.1.1-3-hash":     "0.0.0.0"
        }

        for test, answer in tests.items():
            parse = version.parse(test)
            self.assertEqual(parse, answer, test)