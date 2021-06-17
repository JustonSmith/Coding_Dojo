class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

// FIFO
// First In, First Out

class SLQueue {
    constructor() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    populateRandom(max, length) {
        for (let i = 1; i <= length; i++) {
            let temp = Math.floor(Math.random() * max) + 1;
            this.enqueue(temp);
        }
        return this;
    }

    isEmpty() {
        return this.head === null;
    }

    printVals() {
        if (this.isEmpty()) {
            console.log('Queue is empty.')
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

    // SLQueue: Enqueue
    // Create SLQueue method enqueue(val) to add the given value to end of our queue.
    
    enqueue(val) {
        const newTail = new Node(val);

        if (this.isEmpty()) {
            this.head = newTail;
            this.tail = newTail;

        } else {
            this.tail.next = newTail;
            this.tail = newTail;
        }

        this.size++;
        return this;
    }
}