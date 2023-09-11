import omni.ui as ui
import omni.ext
from omni.ui import color as cl

class BitoneBsiSystemLogin():
    
    def __init__(self, vp:ui.Window, ext_id):
        
        self._vp = vp

        self._width = vp.width / 2
        self._frame = self._vp.get_frame(ext_id)

        
        self._logo = "c:/Users/Jiucao/Desktop/Logo/Cuijustudio_Logo.png"
        
        self._frame.set_build_fn(self.login_page)
        
    

    def login_page(self):
        with ui.ZStack():
                ui.Rectangle(style = {"background_color":cl(0.2,0.2,0.2,)})
                with ui.Placer(offset_x = 576, offset_y = 197):
                    with ui.VStack():
                        with ui.Frame(width = 768, height = 444, vertical_clipping = True):
                            with ui.VStack():
                                ui.Image(self._logo, width = 768, height = 222, alignment = ui.Alignment.CENTER, style = {"border_radius":10})
                                ui.Label("BITONE SERVICESHOP", width = 768, height = 76,alignment = ui.Alignment.CENTER,
                                    style = {
                                        "font_size":72,
                                            })
                                ui.Label("Image", width = 768, height = 76,alignment = ui.Alignment.CENTER,
                                    style = {
                                        "font_size":72,
                                            })
                with ui.Placer(offset_x = 688, offset_y = 671):
                    with ui.Frame(width = 449, height = 120):
                        with ui.VStack():
                            with ui.HStack():
                                ui.Label("User",height = 50, alignment = ui.Alignment.CENTER,style = {
                                    "font_size":22,
                                    "padding": 10,
                                        })
                                self.username = ui.StringField(width = 353 , height = 50, style = {"border_radius":10,
                                                                                "font_size":26,
                                                                                "color" :cl.black,
                                                                                "background_color":cl.white})
                                
                            with ui.HStack():
                                ui.Label("PassWord",height = 50, alignment = ui.Alignment.LEFT_CENTER,style = {
                                    "font_size":22,
                                    "padding": 10,
                                        })
                                self.userpass = ui.StringField(width = 353 , height = 50, style = {"border_radius":10,
                                                                                "font_size":26,
                                                                                "color" :cl.black,
                                                                                "alignment":ui.Alignment.LEFT_CENTER,
                                                                                "background_color":cl.white})
                            
                            self.username.model.add_value_changed_fn(
                                lambda m:self.print_user_account(m.get_value_as_string())
                            )
                            
                            self.userpass.model.add_value_changed_fn(
                                lambda m:self.print_user_account(m.get_value_as_string())
                            )
                
                with ui.Placer(offset_x = 897, offset_y = 829):
                    with ui.ZStack(width = 127, height = 54):
                        ui.Button("Login" ,clicked_fn = self.Switch_page,
                                style = {"border_radius":25,"background_color":cl.black,
                                        "font_size":20,
                                        "color":cl.white})

    def print_user_account(self, name):
        
        print(f"{name}")
    
    def Switch_page(self):
        self._frame.set_build_fn(self.second_page)
        
    def Switch_back(self):
        self._frame.set_build_fn(self.login_page)
    
    def second_page(self):
        with ui.VStack():
            ui.Spacer(height = ui.Percent(50))
            with ui.HStack():
                ui.Spacer(width = ui.Percent(50))
                ui.Button(width = 200, height = 200, clicked_fn = self.Switch_back, style = {
                "image_url" : "exts/Bitone.BSI.System/data/SVG/circle-heat-svgrepo-com.svg",
            })
    
        
    def destroy(self):
        
        self._vp = None
        
    def __del__(self):
        
        self.destroy()
