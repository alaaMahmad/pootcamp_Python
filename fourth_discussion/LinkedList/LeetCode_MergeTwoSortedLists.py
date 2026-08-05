class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner is not None:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        if self.head is None:
            self.add_to_front(val)
            return self

        new_node = SLNode(val)
        runner = self.head
        while runner.next is not None:
            runner = runner.next

        runner.next = new_node
        return self

    def remove_from_front(self):
        if self.head is None:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        return removed_value

    def remove_from_back(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return self.remove_from_front()

        runner = self.head
        while runner.next.next is not None:
            runner = runner.next

        removed_value = runner.next.value
        runner.next = None
        return removed_value

    def remove_val(self, val):
        if self.head is None:
            return None

        if self.head.value == val:
            self.remove_from_front()
            return self

        runner = self.head
        while runner.next is not None:
            if runner.next.value == val:
                runner.next = runner.next.next
                return self
            runner = runner.next

        return self

    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
            return self

        new_node = SLNode(val)
        runner = self.head
        count = 0

        while runner is not None and count < n - 1:
            runner = runner.next
            count += 1

        if runner is not None:
            new_node.next = runner.next
            runner.next = new_node

        return self

    def merge_two_lists(self, list1, list2):
        list_3 = SLNode(0)
        tail = list_3

        runner_1 = list1.head
        runner_2 = list2.head

        while runner_1 is not None and runner_2 is not None:
            if runner_1.value <= runner_2.value:
                tail.next = runner_1
                runner_1 = runner_1.next
            else:
                tail.next = runner_2
                runner_2 = runner_2.next
            tail = tail.next

        if runner_1 is not None:
            tail.next = runner_1
        else:
            tail.next = runner_2

        merged_slist = SList()
        merged_slist.head = list_3.next
        return merged_slist


print("Test 1: Standard Lists ")
list1 = SList()
list1.add_to_back(1)
list1.add_to_back(2)
list1.add_to_back(4)

list2 = SList()
list2.add_to_back(1)
list2.add_to_back(3)
list2.add_to_back(4)

slist_runner = SList()
merged1 = slist_runner.merge_two_lists(list1, list2)
merged1.print_values()


print("\nTest 2: Different Lengths")
list3 = SList()
list3.add_to_back(1)
list3.add_to_back(5)
list3.add_to_back(10)
list3.add_to_back(15)

list4 = SList()
list4.add_to_back(2)
list4.add_to_back(3)

merged2 = slist_runner.merge_two_lists(list3, list4)
merged2.print_values()


print("\nTest 3: One Empty List")
list5 = SList() 

list6 = SList()
list6.add_to_back(0)
list6.add_to_back(8)
list6.add_to_back(9)

merged3 = slist_runner.merge_two_lists(list5, list6)
merged3.print_values()