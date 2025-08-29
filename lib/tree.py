class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)
    
    def get_element_by_id(self, target_id):
        # Check if current node matches the target ID
        if self.value.get('id') == target_id:
            return self.value
        
        # Recursively search through all children
        for child in self.children:
            result = child.get_element_by_id(target_id)
            if result is not None:
                return result
        
        # Return None if not found in this branch
        return None