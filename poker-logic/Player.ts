import { Card } from "./Card"


export class Player {
    stack: number
    hand: Card[] = []
    name: string

    constructor(name: string, stack: number) {
        this.name = name
        this.stack = stack
    }
}