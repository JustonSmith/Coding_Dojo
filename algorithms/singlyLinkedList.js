
// // Singly Linked List

// class Node{
//     constructor(val){
//         this.val = val;
//         this.next = null;
//     }
// }

// class SinglyLinkedList{
//     constructor() {
//         this.head = null;
//     }

//     addFront(val){
//         const newHead = new Node(val);
//         newHead.next = this.head;
//         this.head = newHead;
//         return this;
//     }

//     addBack(val){
//         const newTail = new Node(val);
//         let runner = this.head;

//         if(runner === null){
//             this.head = newTail
//         } else {
//             while(runner.next) {
//                 runner = runner.next;
//             }
//             runner.next = newTail;
//         }
//         return this;
//     }

//     printVals(){
//         let runner = this.head;
//         while(runner) {
//             console.log(runner.val);
//             runner = runner.next;
//         }
//         return this;
//     }

// let mySll = new SinglyLinkedList
// console.log(mySll);

// mySll.addFront(4).addFront(2).addFront(8).addFront(7);
// mySll.printVals();
// mySll.addBack(5).addBack(8). addBack(2);



// let myNode = new Node(8);
// console.log(myNode);
// let newNode = new Node(2);
// console.log(newNode);
// myNode.next = newNode;
// console.log(`myNode's next node's value is now: ${myNode.next.val}`)


// // SLList: Contains
// // Given a value, return true if that value is found in any node in the singly linked list. Return false if it is not.

//     contains(val){
//     let runner = this.head;
//     while(runner){
//         if(runner.val === val) {
//             console.log(true);
//             return true;
//         }
//         runner = runner.next;
//         }
//     return false;
//     }
// }

// let newList = new SlinglyLinkedList()
// newList.addFront(11).addFront(45).addBack(100).addFront(21).addFront(5)
