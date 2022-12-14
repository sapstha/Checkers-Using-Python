# Module: pieces.py
# Student Name: Sapana Shrestha
# Student ID: 00710117
# Description:Piece class to maintain all the pieces
# Python Version: 3.10.7
class Piece:

    #Default constructor for the Piece Class with row,column value and piece type(x or o)
    def __init__(self, row_loc, col_loc, pieceType):
        self.locRow = row_loc
        self.locCol = col_loc
        self.pieceType = pieceType

    #This function sets new position for a given piece
    def set_location(self, row, col):
        self.locRow = row
        self.locCol = col
    
    #This function gets the position of a given piece with row,column values
    def get_location(self):
        return [self.locRow, self.locCol]
    
    #This function sets the type(x or o) for the piece
    def set_type(self, newType):
        self.pieceType = newType
    
    #This function gets the type(x or o) of the piece
    def get_type(self):
        return self.pieceType