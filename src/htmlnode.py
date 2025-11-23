class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f'{self.tag}, {self.value}, {self.children}, {self.props}'
        
class LeafNode(HTMLNode):
        def __init__(self,tag,value,props=None):
            super().__init__(tag=tag, value=value, children=None, props=props)
            self.props = props
        def to_html(self):
            if self.value is None:
                raise ValueError('value can not be None')
            if self.tag is None:
                return self.value
            props = self.props_to_html()
            return f'<{self.tag}{props}>{self.value}</{self.tag}>'
          
        def __repr__(self):
            return f"LeafNode({self.tag}, {self.value}, {self.props})"
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        self.props = props
    def to_html(self):
        if self.tag is None:
            raise ValueError('Need a tag')
        if self.children is None:
            raise ValueError('Need a children tag')
        inner = ""
        for child in self.children:
            inner += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{inner}</{self.tag}>' 
        
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"