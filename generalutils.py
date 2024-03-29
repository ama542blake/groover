from typing import Collection, List, Sized

def get_length_of_longest_item(items: Collection[Sized]) -> int:
    return max(map(lambda item: len(item), items))