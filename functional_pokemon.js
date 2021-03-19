class Pokemon {

	constructor(name, cry){
		this.name = name
		this.cry = cry
	}

	makeCry() {
		return `${this.name} cries ${this.cry}`
	}

	faint(){
		return `${this.name} cries ${this.cry} and faints`
	}

}

function PokemonGenerator(name, cry){
	return {
		name: name,
		cry: cry, 
		makeCry: function (){
			return `${this.name} cries ${this.cry}`
		},

		faint: function(){
			return `${this.name} cries ${this.cry} and faints`
		}
	}
}


pikachu = new Pokemon("pikachu", "pika")
console.log(pikachu.makeCry())
console.log(pikachu.faint())
console.log(pikachu.name)
console.log(pikachu)

// this is implements the the behavior as a class
pikachuObject = PokemonGenerator("pikachu", "pika")
console.log(pikachuObject.makeCry())
console.log(pikachuObject.faint())
console.log(pikachuObject.name)
console.log(pikachuObject)

// this really behave like you'd expect from a class instance
pikachuObject.cry = "pikapika"
console.log(pikachuObject.cry)
console.log(pikachuObject.makeCry())



