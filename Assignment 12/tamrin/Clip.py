from Mediaa import Mediaa

class Clip(Mediaa):
    def __init__(self,co,n,d,i_s,u,dura,c,N_o_episodes,Year_of_construction,location,date):
        super().__init__(c,n,d,i_s,u,dura,c)
        
    def show_info():
        print(self.code)
        print(self.name)
        print(self.director)
        print(self.IMDBscore)
        print(self.url)
        print(self.duration)
        print(self.casts)
        print(self.N_o_episodes)
        print(self.Year_of_construction)
        print(self.location)
        print(self.data)