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
        editor2 = anvil.js.get_dom_node(self.column_panel_3)
        jQuery( "#anvil-header" ).remove()
        # add a ColumnPanel in the design view
        # get the dom node for the ColumnPanel
        self.quill = Quill( editor, {
            'modules': { 'toolbar': True },
            'theme': 'snow'
        })
        self.quill2 = Quill( editor2, {
            'modules': { 'toolbar': True },
            'theme': 'snow'
        })
        
        self.quill2.on('text-change2', self.text_change)
        
    def text_change(self, delta, old_delta, source):
        print(source, self.quill.getText())

    def text_change2(self, delta, old_delta, source):
        print(source, self.quill2.getText())

    def form_show(self, **event_args):
        """This method is called when the HTML panel is shown on the screen"""
        jQuery( ".app-bar" ).css( "top", "0px" )
        jQuery( ".content" ).css( "margin-top", "9px" )

