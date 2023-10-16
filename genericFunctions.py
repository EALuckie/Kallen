#Libraries
import youtube_dl
#Global variables and settings

class YouTube:
    #Variables
    #settings= 

    def __init__(self,name) -> None:
        self.name= name

    def getName(self):
        return self.name

class ChatGPT:
    #
    def __init__(self) -> None:
        pass
        
class Db:
    #
    def __init__(self) -> None:
        pass

def main():
    """Main function for class testing"""
    
    n= YouTube("Sheshe")
    print(n.getName())
    del n
    print(n.getName())

    return

main()