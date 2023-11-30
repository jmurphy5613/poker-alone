import { Card } from "./Card";
import { Deck } from "./Deck";
import { Player } from "./Player";


class Game {
    players: Player[] = []
    deck: Deck = new Deck()

    toString(): string {
        return `
            Players: ${this.players.map((player: Player) => player.name).join(", ")}
            Deck: ${this.deck.deck.map((card: Card) => card.toString()).join(", ")}
        `
    }

    resest(): void {
        this.deck = new Deck()
        this.players.forEach((player: Player) => {
            player.hand = []
        })
    }

    constructor(stack: number, names: string[]) {
        names.forEach((name: string) => {
            this.players.push(new Player(name, stack))
        })
    }
}

