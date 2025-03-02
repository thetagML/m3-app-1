from ._anvil_designer import Form1Template
from anvil import *
from anvil.js.window import Quill 
import anvil.js
from anvil.js.window import jQuery

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
    
        # Any code you write here will run before the form opens.
        editor = anvil.js.get_dom_node(self.column_panel_1)
        jQuery( "#anvil-header" ).remove()
        # add a ColumnPanel in the design view
        # get the dom node for the ColumnPanel
        self.quill = Quill( editor, {
            'modules': { 'toolbar': True },
            'theme': 'snow'
        })
        
        self.quill.on('text-change', self.text_change)
        
    def text_change(self, delta, old_delta, source):
        print(source, self.quill.getText())