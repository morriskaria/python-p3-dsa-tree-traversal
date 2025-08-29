import sys
import os

# Add the parent directory to the path to import tree
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from tree import Tree

def test_get_element_by_id():
    """Test the get_element_by_id method"""
    
    # Build test tree
    root = Tree({
        'tag_name': 'body',
        'id': None,
        'text_content': None
    })
    
    heading = Tree({
        'tag_name': 'h1',
        'id': 'heading',
        'text_content': 'Title'
    })
    
    div = Tree({
        'tag_name': 'div',
        'id': 'container',
        'text_content': None
    })
    
    paragraph = Tree({
        'tag_name': 'p',
        'id': 'content',
        'text_content': 'Some text'
    })
    
    # Build the tree structure
    root.add_child(heading)
    root.add_child(div)
    div.add_child(paragraph)
    
    # Test finding the heading
    result = root.get_element_by_id('heading')
    expected = {
        'tag_name': 'h1',
        'id': 'heading',
        'text_content': 'Title'
    }
    
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test finding the paragraph
    result = root.get_element_by_id('content')
    expected = {
        'tag_name': 'p',
        'id': 'content',
        'text_content': 'Some text'
    }
    
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Test non-existent ID
    result = root.get_element_by_id('nonexistent')
    assert result is None, f"Expected None, but got {result}"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_get_element_by_id()