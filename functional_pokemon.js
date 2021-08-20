/**
 * ES6 Class representing a Pokemon.
 */
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

/**
 * Mutable "Class" representing a Pokemon.
 */
function MutablePokemonGenerator(name, cry){
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

/**
 * Immutable "Class" representing a Pokemon.
 */
 function ImmutablePokemonGenerator(name, cry){
	return Object.freeze({
		makeCry: function (){
			return `${name} cries ${cry}`
		},

		faint: function(){
			return `${name} cries ${cry} and faints`
		}
	})
}

// demo of ES6 class
let pikachu = new Pokemon("pikachu", "pika")
console.log(pikachu.makeCry())
console.log(pikachu.faint())
console.log(pikachu.name)
console.log(pikachu)
pikachu.cry = "pikapika"
console.log(pikachu.makeCry())

// demo of mutable "class" 
let pikachuObjectMutable = MutablePokemonGenerator("pikachu", "pika")
console.log(pikachuObjectMutable.makeCry())
console.log(pikachuObjectMutable.faint())
console.log(pikachuObjectMutable.name)
console.log(pikachuObjectMutable)
pikachuObjectMutable.cry = "pikapika"
console.log(pikachuObjectMutable.makeCry())

// demo of immutable "class" 
let pikachuObjectImmutable = ImmutablePokemonGenerator("pikachu", "pika")
console.log(pikachuObjectImmutable.makeCry())
console.log(pikachuObjectImmutable.faint())
console.log(pikachuObjectImmutable.name)
console.log(pikachuObjectImmutable)
pikachuObjectImmutable.cry = "pikapika" // this doesn't do anything because the object is frozen
console.log(pikachuObjectImmutable.makeCry()) // same as last time
console.log(pikachuObjectImmutable) // same as last time
