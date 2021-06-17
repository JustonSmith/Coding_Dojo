

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

    populateRandom(max, length) {
        for (let i = 1; i <= length; i++) {
            let temp = Math.floor(Math.random() * max) + 1;
            this.addFront(temp);
        }
        return this;
    }

    addFront(val) {
        const newHead = new Node(val);
        newHead.next = this.head;
        this.head = newHead;
        return this;
    }

    contains(val) {
        if (this.isEmpty()) {
            console.log("This SLL is empty.")
            return this;
        } else {
            let runner = this.head;
            while (runner) {
                if (runner.val === val) {
                    console.log(`Value (${val}) found.`)
                    return true;
                }
                runner = runner.next;
            }
            console.log(`Value (${val}) not found.`)
            return false;
        }
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

// SLList: Remove Negatives
// Create a function that removes all negative values from a list, then return the modified list.

// Second to Last Value
// Create a function that returns the value in the second-to-last node.

// Partition
// Create a function that, given a value, locates the first node with that value, moves all nodes with values less than that value to be earlier, and moves all nodes with values greater than that value to be later. Otherwise, original order need not be perfectly preserved. Return the list when complete.

// lowerList, higherList
// Traverse the list and 

// 2 > 8 > 1 > 4 > 10 > 9 > 5
// 2 > 1 > 4 > 8 > 10 > 9 > 5