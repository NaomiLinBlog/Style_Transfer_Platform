from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def input_image_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    anvil.server.call('get_input_img',file)
    self.content.source = file
    
  def style_image_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    anvil.server.call('get_style_img',file)
    self.style.source = file

  def start_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('start_style_transfer')
    print("start")
    output_img = anvil.server.call('getimage')
    self.output.source = output_img
    print("finish")

  




  
  

