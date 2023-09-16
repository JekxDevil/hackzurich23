import re

from filecrawler.rulebase import RuleBase


class RSA(RuleBase):

    def __init__(self):
        super().__init__('rsa-private-key', 'RSA')

        self._regex = re.compile(r"-----BEGIN (?:RSA )?PRIVATE KEY-----[\s\S]*?-----END (?:RSA )?PRIVATE KEY-----")
        self._keywords = ["PRIVATE KEY"]
        self._exclude_keywords = [
            "EXAMPLE"  # AKIAIOSFODNN7EXAMPLE
        ]

