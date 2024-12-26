"""
Abstract class for fetching data from different providers
"""

from abc import ABC, abstractmethod
from parsers.api_result import ApiResult


class ApiClient(ABC): 
    """Abstract class for fetching data from different providers"""

    @abstractmethod
    def work(self, message: str, **args) -> ApiResult:
        """
        Async method for fetching data
        :param word: Word to be searched, as typed into the search bar
        :return: Data container inhering from ApiResult with the results
        """
        