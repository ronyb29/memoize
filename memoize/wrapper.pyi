from typing import Callable, TypeVar, overload, Optional

from memoize.configuration import CacheConfiguration
from memoize.invalidation import InvalidationSupport

FN = TypeVar('FN', bound=Callable)


@overload
def memoize(*,
            configuration: Optional[CacheConfiguration] = None,
            invalidation: Optional[InvalidationSupport] = None) -> Callable[[FN], FN]: ...


@overload
def memoize(method: FN,
            configuration: Optional[CacheConfiguration] = None,
            invalidation: Optional[InvalidationSupport] = None) -> FN: ...
