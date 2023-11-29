export enum Suit {
    Hearts,
    Diamonds,
    Spades,
    Clubs
}

export enum Rank {
    Ace,
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    Ten,
    Jack,
    Queen,
    King
}

export class Card {

    readonly suit: Suit
    readonly rank: Rank

    constructor (suit: Suit, rank: Rank) {
        this.suit = suit
        this.rank = rank
    }
}