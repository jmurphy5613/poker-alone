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

    constructor() {
        this.deck = this.createDeck();
    }
}