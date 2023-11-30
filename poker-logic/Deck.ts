import { Card, Suit, Rank } from "./Card";

export class Deck {

    deck: Card[] = [];

    createDeck(): Card[] {
        let suits = Object.values(Suit) as Suit[];
        let ranks = Object.values(Rank) as Rank[];
        //filter out the numerical values of the enums
        suits = suits.filter((suit: Suit) => typeof suit === "string");
        ranks = ranks.filter((rank: Rank) => typeof rank === "string");
        
        const deckToReturn: Card[] = [];
        suits.forEach((suit: Suit) => { // Explicitly cast suit to Suit
            ranks.forEach((rank: Rank) => {
                deckToReturn.push(new Card(suit, rank));
            });
        });
        return deckToReturn;
    }

    shuffleDeck(): void {
        // Fisher-Yates shuffle

        const newDeck: Card[] = [];
        while (this.deck.length > 0) {
            const randomIndex = Math.floor(Math.random() * this.deck.length);
            const randomCard = this.deck.splice(randomIndex, 1)[0];
            newDeck.push(randomCard);
        }
        this.deck = newDeck;

        // for (let i = this.deck.length - 1; i > 0; i--) {
        //     const j = Math.floor(Math.random() * (i + 1));
        //     const tempCard = this.deck[i];
        //     this.deck[i] = this.deck[j];
        //     this.deck[j] = tempCard;
        // }
    }

    deal(): Card {
        return this.deck.pop() as Card;
    }

    constructor() {
        this.deck = this.createDeck();
    }
}