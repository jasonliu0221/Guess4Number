from random import shuffle

class GuessGame:
	def __init__(self):
		self.set_game()
	def set_game(self):
		self.answer=[chr(i) for i in range(48,58)]
		shuffle(self.answer)
		self.answer=self.answer[0:4]
	def run(self):
		self.times=0
		while True:
			self.times+=1
			guess=raw_input("n:")
			if len(guess)!=4:
				print "wrong length"
				continue
			elif self.checkrepeat(guess):
				print "repeating digits"
				continue
			else:
				self.checkguess(guess)
				if self.a==4:
					print "Correct! Congratulations!"
					break
				else:
					print str(self.a)+"A"+str(self.b)+"B"
		print "you guess "+ str(self.times)+ " times"
		
	def checkrepeat(self, list):
		for i in list:
			if list.count(i)>1:
				return True
		return False		
	def checkguess(self,guess):
		self.a=0
		self.b=0
		for i in guess:
			if i in self.answer:
				if guess.index(i)==self.answer.index(i):
					self.a+=1
				else:
					self.b+=1	
	
if __name__=="__main__":
	g=GuessGame()
	print g.answer
	g.run()