"""You can use currying to replicate the behavior of some classes."""

class Pokemon:

	def __init__(self, sound):
		self.sound =  sound

	def cry(self):
		return self.sound

def make_pokemon(sound):

	def cry():
		return sound

	return cry

def pokemon_cry(sound):
	return sound

if __name__ == "__main__":

	pikachu = Pokemon("Pika")
	assert pikachu.cry() == "Pika"

	pikachu_cry = make_pokemon("Pika")
	assert pikachu_cry() == "Pika"

	assert pokemon_cry("Pika") == "Pika"