class HTMLNode:
    def __init__(self,  tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}
    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return " " + props_str
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class leafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.tag is None:
            return self.value or ""
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"leafNode(tag={self.tag}, value={self.value}, props={self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if not self.children:
            raise ValueError("Parent nodes must have children")
        props_str = self.props_to_html()
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"