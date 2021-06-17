// Day 2

// SLList: Remove Head
// Create a function that removes the head node from a singly linked list.

// SLList: Remove Tail
// Create a function that removes the tail node from a singly linked list.

class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
    }

    addBack(val){
        const newTail = new Node(val);
        let runner = this.head;

        if(runner === null){
            this.head = newTail
        } else {
            while(runner.next) {
                runner = runner.next;
            }
            runner.next = newTail;
        }
        return this;
    }

    populateRandom(max, length) {
        for (let i = 0; i <= length; i++) {
            let temp = Math.floor(Math.random() * max) + 1;
            this.addBack(temp);
        }
        return this;
    }

    isEmpty() {
        return this.head === null;
    }

    printVals() {
        if (this.isEmpty()) {
            console.log("This SLL is empty.")
            return this;
        } else {
            let runner = this.head;
            let output = `**********\n`
            while (runner) {
                output += `${runner.val.toString()} > `;
                runner = runner.next;
            }
            console.log(output);
        }   
        return this;
    }
}

let mySLL = new SinglyLinkedList()
mySLL.populateRandom(200, 20).printVals()

