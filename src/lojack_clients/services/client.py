import ssl
import uuid
from typing import Dict, Union

import attr


@attr.s(auto_attribs=True)
class Client:
    """A class for keeping track of data related to the API"""

    base_url: str = "https://services.spireon.com/v0/rest"
    cookies: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    headers: Dict[str, str] = attr.ib(
        default={"X-Nspire-Apptoken": "eyJzeXN0ZW1JZCI6MjMsImJyYW5kSWQiOjgxfQ=="},
        kw_only=True,
    )
    timeout: float = attr.ib(5.0, kw_only=True)
    verify_ssl: Union[str, bool, ssl.SSLContext] = attr.ib(True, kw_only=True)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        return {"X-Nspire-Correlationid": str(uuid.uuid4()), **self.headers}

    def with_apptoken(self, apptoken: str) -> "Client":
        """Set X-Nspire-Apptoken header"""
        return self.with_headers({"X-Nspire-Apptoken": apptoken})

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        return attr.evolve(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "Client":
        """Get a new client matching this one with a new timeout (in seconds)"""
        return attr.evolve(self, timeout=timeout)


@attr.s(auto_attribs=True)
class AuthenticatedClient(Client):
    """A Client which has been authenticated for use on secured endpoints"""

    @classmethod
    def from_token(cls, usertoken: str):
        """Create a new client instance from a usertoken"""
        return cls().with_token(usertoken)

    def with_token(self, usertoken: str) -> "Client":
        """Set X-Nspire-Usertoken authentication header"""
        return self.with_headers({"X-Nspire-Usertoken": usertoken})
