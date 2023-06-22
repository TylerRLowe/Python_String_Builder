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
        
