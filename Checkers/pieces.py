# Class to maintain pieces
class Piece:

    # Default constructor
    def __init__(self, row_loc, col_loc, pieceType):
        self.locRow = row_loc
        self.locCol = col_loc
        self.pieceType = pieceType

    # Method to set new location for piece
    def set_location(self, row, col):
        self.locRow = row
        self.locCol = col
    
    # Method to get the location of the piece
    def get_location(self):
        return [self.locRow, self.locCol]
    
    # Method to set the type of piece
    def set_type(self, newType):
        self.pieceType = newType
    
    # Method to get the type of piece
    def get_type(self):
        return self.pieceType