@lru_cache(maxsize=128)
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """두 수의 합을 반환하는 함수"""
    return a + b
