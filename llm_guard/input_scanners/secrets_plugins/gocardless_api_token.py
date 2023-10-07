"""
This plugin searches for GoCardless API tokens.
"""

import re

from detect_secrets.plugins.base import RegexBasedDetector


class GoCardlessApiTokenDetector(RegexBasedDetector):
    """Scans for GoCardless API Tokens."""

    secret_type = "GoCardless API Token"

    denylist = [
        # GoCardless API token
        re.compile(
            r"""(?i)(?:gocardless)(?:[0-9a-z\-_\t .]{0,20})(?:[\s|']|[\s|"]){0,3}(?:=|>|:{1,3}=|\|\|:|<=|=>|:|\?=)(?:'|\"|\s|=|\x60){0,5}(live_(?i)[a-z0-9\-_=]{40})(?:['|\"|\n|\r|\s|\x60|;]|$)"""
        ),
    ]
