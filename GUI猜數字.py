from Tkinter import *
from guessgame import *

class GuessGameGui(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.grid()
		self.set_Frame()
		
		self.game=None
		self.times=0
	
	def set_Frame(self):
		self.ip=Label(self)
		self.ip["text"]="Input 4 digits: "
		self.ip.grid(row=0,column=0)
		
		self.ie=Entry(self)
		self.ie["width"]=16
		self.ie.grid(row=0,column=1,columnspan=5)
		
		self.nb=Button(self)
		self.nb["text"]="NewGame"
		self.nb.grid(row=1,column=0)
		self.nb["command"]=self.new_game
		
		self.cb=Button(self)
		self.cb["text"]="CheckGame"
		self.cb.grid(row=1,column=1,columnspan=5)
		self.cb["command"]=self.checkgame
		
		self.show1=Label(self)
		self.show1["text"]="Welcom to Guess Game!"
		self.show1.grid(row=2,column=0,columnspan=8)

		self.show2=Label(self)
		self.show2["text"]=""
		self.show2.grid(row=3,column=0,columnspan=8)
		
	def	checkgame(self):
		if self.game == None:
			self.show1["text"]="Press the \"NewGame\" button first!"
			self.show2["text"]=""
		else:
			self.guess=self.ie.get()
			self.times+=1
			if len(self.guess)!=4:
				self.show1["text"]="Wrong length !"
			elif self.game.checkrepeat(self.guess):
				self.show1["text"]="Repeating digits !"
			else:
				self.game.checkguess(self.guess)
				if self.game.a==4:
					self.show1["text"]="Correct! Congratulations!"
					self.show2["text"]="you guess "+str(self.times)+" times"
					self.game = None
					self.times=0
				else:
					self.show1["text"]=str(self.game.a)+"A"+str(self.game.b)+"B"
					
	
	def	new_game(self):
		self.game=GuessGame()
		self.show1["text"]="New Game starting! GO!"
		self.show2["text"]=self.game.answer

		
		
if __name__=="__main__":
	root=Tk()
	app=GuessGameGui(master=root)
	app.mainloop()