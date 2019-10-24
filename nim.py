
import random
import time

class CantMove( Exception ) :

    def __init__( self, reason ) :
        self. __reason = reason

    def __repr__( self ) :
        return "unable to find a move: {}". format( self.__reason )


class Nim :
    
    def __init__( self, startstate ) :
        self. state = startstate

    def __repr__( self ) :
        
        index = 0
        row = 1
        string = ""
        
        while index < len( self.state ) :
            
            counter = 0
            string = string + ( "{} :". format( row ) )
            
            while counter < self.state[ index ] :
                
                string = string + " 1"
                counter += 1
            
            string = string + "\n"
            row += 1
            index += 1
        
        return string

    def sum( self ) :
        
        index = 0
        sum = 0
        
        while index < len( self.state ) :
            
            sum = sum + self.state[ index ]
            index += 1
        
        return sum

    def nimber( self ) :
        
        index = 0
        nmb = 0
        
        while index < len( self.state ) :
            
            nmb = nmb ^ self.state[ index ]
            index += 1
        
        return nmb

    def randommove( self ) :
        
        if self.sum( ) != 0 :
            
            row = random.randrange( len( self.state ) )
            
            while self.state[ row ] == 0 :
                row = random.randrange( len( self.state ) )
            
            self.state[ row ] = self.state[ row ] - random.randint( 1, self.state[ row ] )
    
        else :
            raise CantMove( "no sticks left" )

    def removelastmorethantwo( self ) :
    
        index = 0
        counter1 = 0
        countermorethan1 = 0
        
        while index < len( self.state ) :
            
            if self.state[ index ] > 1 :
                countermorethan1 += 1
                indexmorethan1 = index
            
            if self.state[ index ] == 1 :
                counter1 += 1
    
            index += 1
    
        if countermorethan1 == 1 :
            
            if counter1 % 2 == 0 :
                self.state[ indexmorethan1 ] = 1
    
            else :
                self.state[ indexmorethan1 ] = 0
    
        else :
            raise CantMove( "more than one row has more than one stick" )

    def makenimberzero( self ) :
        
        if self.nimber( ) != 0 :
            
            row = random.randrange( len( self.state ) )
            
            while ( self.state[ row ] ^ self.nimber() ) >= self.state[ row ] :
                    row = random.randrange( len( self.state ) )
            
            self.state[ row ] = self.state[ row ] ^ self.nimber()

        else:
            raise CantMove( "nimber is already zero" )
        
    def optimalmove( self ) :
        
        try :
            self.removelastmorethantwo( )
        
        except CantMove:
            
            try :
                self.makenimberzero( )
            
            except CantMove :
                self.randommove( )

    def usermove( self ) :
        
        inputRow = input( "Please make a move, select the row :")
            
        try :
               
            row = int( inputRow )

            if row > len(self.state) or row <= 0 or self.state[ row - 1 ] == 0:
                
                print( "Please, try again! You entered invalid row number" )
                self.usermove( )
                return

            inputStick = input( "Please enter number of remaining sticks :" )

            stick = int( inputStick )
                    
            if stick < 0 or stick >= self.state[ row - 1 ] :
                    
                print( "Please, try again! You enetered invalid number of remaining sticks" )
                self.usermove( )
                return
            
        except ValueError :
            
            print( "Please, try again! You entered not integer input" )
            self.usermove( )
            return

        self.state[ row - 1 ] = stick

def play( ) :
    
    st = Nim( [ 1, 2, 3, 4, 5, 6 ] )

    turn = "user"
    
    while st. sum( ) > 1 :
        
        if turn == "user" :
            
            print( "\n" )
            print( st )
            print( "hello, user, please make a move" )
            st. usermove( )
            turn = "computer"
        
        else :
            
            print( "\n" )
            print( st )
            print( "now i will make a move\n" )
            print( "thinking" )
            
            for r in range( 15 ) :
                
                print( ".", end = "", flush = True )
                time. sleep( 0.1 )
            
            print( "\n" )

            st. optimalmove( )
            turn = "user"

    print( "\n" )
    
    if turn == "user" :
        print( "you lost\n" )
    
    else :
        print( "you won\n" )
