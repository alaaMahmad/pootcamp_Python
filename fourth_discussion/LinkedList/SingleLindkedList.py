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

linked_list = SList()

linked_list = SList()

print("Testing add_to_front")
linked_list.add_to_front("alaa")
linked_list.add_to_front("hello")
linked_list.print_values()

print("\nTesting add_to_back")
linked_list.add_to_back("world")
linked_list.print_values()

print("\nTesting insert_at index 1")
linked_list.insert_at("python", 1)
linked_list.print_values()

print("\nTesting remove_from_front")
removed_front = linked_list.remove_from_front()
print(f"Removed: {removed_front}")
print("List now:")
linked_list.print_values()

print("\nTesting remove_from_back")
removed_back = linked_list.remove_from_back()
print(f"Removed: {removed_back}")
print("List now:")
linked_list.print_values()

print("\nTesting remove_val python")
linked_list.remove_val("python")
linked_list.print_values()