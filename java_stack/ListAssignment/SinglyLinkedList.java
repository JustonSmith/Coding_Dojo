package java_stack.ListAssignment;

public class SinglyLinkedList {
    public Node head;

    public SinglyLinkedList() {
        this.head = null;
    }

    public void add(int value) {
        Node newNode = new Node(value);
        if(head == null) {
            head = newNode;
        } else {
            Node runner = head;
            while(runner.next != null) {
                runner = runner.next;
            }
            runner.next = newNode;
        }
    }
    public void remove(){
        if(head.next == null){
        this.head = null;
    }
    Node runner = this.head;
    while(runner.next.next != null){
        runner = runner.next;
    }
    runner.next = null;
}
    public void printValues(){
    Node runner = this.head;
    if(head == null){
        System.out.println("No nodes!");
    }
    while(runner.next != null){
        System.out.println(runner.value);
        runner = runner.next;
    }
    System.out.println(runner.value);
    }
}

//     public  find(int value){
//     Node runner = this.head;
//             if(runner.next.value == value){
//             return runner.value;
//         }
//         while(runner.next != null){
//             if(runner.next.value == value){
//                 return runner.value;
//             }
//             runner = runner.next;
//         }
//     }

//     public void removeAt(int value){
//         Node runner = head;
//         if(value == 0){
//             if(runner.next){
//                 head = runner.next;
//             }
//             else{
//                 head = null;
//             }
//         }
//         while(
//     }
// 





