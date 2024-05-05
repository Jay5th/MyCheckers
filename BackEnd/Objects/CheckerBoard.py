class CheckerBoard:
    def __init__(self, matrix=None, lookup_entry=None):
        if isinstance(lookup_entry, dict):
            self.lookup_entry = lookup_entry
        elif isinstance(matrix, list):
            self.lookup_entry = {}
            for i in range(8):
                for j in range(8):
                    if (i + j) % 2 == 0:
                        continue
                    entry = matrix[i][j]
                    if not (entry is None):
                        self.lookup_entry[(i, j)] = entry
        else:
            self.lookup_entry = {}

    def __str__(self):
        output = " " + "---------- " * 8 + "\n"
        for i in range(8):
            output += "|" + "          |" * 8 + "\n"
            output += "|"
            for j in range(8):
                if (i + j) % 2 == 0:
                    output += "          |"
                elif self.get_entry((i, j)) is None:
                    output += "    00    |"
                else:
                    output += f"    {self.get_entry((i, j))}    |"
            output += "\n" + "|" + "          |" * 8 + "\n"
            if i != 7:
                output += "|" + "----------|" * 8 + "\n"
            else:
                output += " " + "---------- " * 8
        return output

    def get_entry(self, address):
        return self.lookup_entry.get(address)

    def replace_entry(self, address, piece_or_none):
        if piece_or_none is None:
            self.lookup_entry.pop(address)
        else:
            self.lookup_entry[address] = piece_or_none

    def move_piece(self, start_address, end_address):
        assert not (self.get_entry(start_address) is None), f"there is nothing to move at address {start_address}"
        assert self.get_entry(end_address) is None, f"the address {end_address} is not available to be moved to"
        piece = self.get_entry(start_address)
        self.replace_entry(end_address, piece)
        self.replace_entry(start_address, None)
