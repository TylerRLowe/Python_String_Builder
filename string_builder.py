import typing

class StringBuilder:
    """
    StringBuilder class provides efficient string building capabilities.

    Attributes:
        buffer (List[str]): A list to store the string fragments.
        len (int): The current length of the concatenated string.
    """

    def __init__(self, string: str = '', capacity: int = float('inf')) -> None:
        """
        Initializes a StringBuilder object.

        Args:
            string (str): Optional initial string for the buffer (default: '').
            max_length (int): Optional maximum length allowed for the concatenated string (default: -1).

        Returns:
            None
        """
        self.buffer = list(string)
        self.max_length = capacity
        self.count = len(string)
        

    def append(self, string: str) -> None:
        """
        Appends the given text to the buffer aslong as it is under the max length.

        Args:
            text (str): The text to be appended.

        Returns:
            None
        """
        if(self.count + len(string) > self.max_length): return
        self.buffer.append(string)
        self.count += len(string)

    def __str__(self) -> str:
        """
        Returns the concatenated string.

        Returns:
            str: The concatenated string.
        """
        string = ''.join(self.buffer)
        return string
    
    def __len__(self) -> int:
        """
        Returns the length of the string.
        
        Returns:
            int: the length of the string.
        """
        return self.count
    
    def capacity(self):
        """
        Returns the max capacity of the string builder.
        
        Returns:
            int: the max capicity.
        """
        return self.max_length
    
    def set_capacity(self, new_max_length: int) -> None:
        """
        Sets the maximum length of the string builder.
        If it currently exceeds the new max length, it will be trimmed down.

        Args:
            new_max_length (int): The new maximum length allowed for the concatenated string.

        Returns:
            None
        """
        self.max_length = new_max_length
        if self.count > new_max_length:
            self.buffer = self.buffer[:new_max_length]
            self.count = new_max_length
        
    def clear(self):
        """
        Clears the buffer by setting it to an empty list.
        """
        self.buffer = []
        self.count = 0
        
    def delete(self, start: int, end: int):
        """
        Delete characters from this StringBuilder.

        Args:
            start (int): The first character to delete.
            end (int): The index after the last character to delete.

        Raises:
            ValueError: If start or end are out of bounds.
        """
        if start < 0 or start > self.count or start > end:
            raise ValueError("Invalid start index")
        if end > self.count:
            end = self.count
        self.buffer[start:end] = []
        self.count -= end - start
        
    def char_at(self, index: int) -> str:
        """
        Returns the character at the specified index.

        Args:
            index (int): The index of the character.

        Returns:
            str: The character at the specified index.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds")
        return self.buffer[index]
    
    def string_at(self, start: int, length: int) -> str:
        """
        Returns a substring starting from the specified index with the given length.

        Args:
            start (int): The starting index of the substring.
            length (int): The length of the substring.

        Returns:
            str: The substring.

        Raises:
            ValueError: If the start or length values are invalid.
        """
        if start < 0 or start >= self.count:
            raise ValueError("Invalid start index")
        if length < 0:
            raise ValueError("Invalid length")
        end = start + length
        if end > self.count:
            end = self.count
        return ''.join(self.buffer[start:end])