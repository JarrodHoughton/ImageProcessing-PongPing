class Match:
    #Flags
    #Collided with a wall or net
    collidedHorizontally = 0

    #Collided with table or floor
    collidedVertically = 1

    #moving in the same direction
    didntCollide = 2


    #Attribute
    turn = 0
    waitOpposite = 0

    #Objects
    ball = Ball()
    players = []
    tableObjects = []

    #Functions

    #Constructor to add two players in player list
    def __init__(self):
        (self.players).append(Player())
        (self.players).append(Player())
        (self.tableObjects).append(tableObject())
        (self.tableObjects).append(tableObject())
        (self.tableObjects).append(tableObject())

    def defineTable(boundary0, boundary1, boundaryNet, self):
        #The input is three lists of the regions of the table
        #The table is created
        ((self.tableObjects)[0]).createRegion(boundary0)
        ((self.tableObjects)[1]).createRegion(boundary1)
        ((self.tableObjects)[2]).createRegion(boundaryNet)

    def updateGame(point, self):
        #This should have the main logic of the game
        (self.ball).updateBall(point)
        currentPlayer = (self.players)[(self.turn + self.waitOpposite) % 2]
        oppositePlayer = (self.players)[(self.turn + self.waitOpposite + 1) % 2]
        if currentPlayer.isFirstHit():
            if self.didBallHit():
                currentPlayer.doneFirstHit()
                return
            elif self.didBallHitNet():
                oppositePlayer.addPoint()
                currentPlayer.finishServe()
                
                if currentPlayer.didFinishServes():
                    self.switchTurn()
                else:
                    currentPlayer.takeServe()

                return
            elif self.didBallHitOpposite():
                oppositePlayer.addPoint()
                currentPlayer.finishServe()

                if currentPlayer.didFinishServes():
                        self.switchTurn()
                else:
                    currentPlayer.takeServe()

                return  
        else :

            if self.didBallHit():
                oppositePlayer.addPoint()
                currentPlayer.finishServe()

                if currentPlayer.didFinishServes():
                    self.switchTurn()
                else:
                    currentPlayer.takeServe()

                return
            elif self.didBallHitNet():
                if currentPlayer.getLet() == True :
                    currentPlayer.foulLet()
                    return
                else :
                    oppositePlayer.addPoint()
                    currentPlayer.finishServe()

                    if currentPlayer.didFinishServes():
                        self.switchTurn()
                    else:
                        currentPlayer.takeServe()

                    return

            elif self.didBallHitOpposite():
                currentPlayer.foulLet()
                self.switchOpposite()
                return 
#If the ball is out of scope for a certain number of frames could be determined from the ball speed 
#The point is given and serve is closed to start a new serve 
                
    
    def switchTurn(self):
        self.turn = (self.turn + 1)%2
        (players[self.turn]).takeServe()

    def startMatch(self):
        (self.players)[self.turn].takeServe()
     
    def.didBallHit(point, self):
        if ((self.ball).didCollide() == self.collidedVertically) and ((self.tableObjects)[(self.turn + self.waitOpposite) % 2]).inRegion(point):
            return True
        else :
            return False

    def switchOpposite(self):
        self.waitOpposite = (self.waitOpposite + 1)%2

    def didBallHitOpposite(point, self):
        if ((self.ball).didCollide() == self.collidedVertically) and ((self.tableObjects)[(self.turn + self.waitOpposite + 1) % 2]).inRegion(point):
            return True
        else :
            return False

    def didBallHitNet(point, self):
        if ((self.ball).didCollide() == self.collidedHorizontally) and ((self.tableObjects)[2]).inRegion(point):
            return True
        else :
            return False