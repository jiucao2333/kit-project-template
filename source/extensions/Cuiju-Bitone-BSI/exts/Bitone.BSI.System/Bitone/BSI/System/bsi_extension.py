import carb
import omni.ext
from omni.kit.viewport.utility import get_active_viewport_window

from .Login import BitoneBsiSystemLogin

class BitoneBsiSystemExtension(omni.ext.IExt):
    
    def on_startup(self, ext_id):
        
        vp = get_active_viewport_window()
        
        vp.height , vp.width = 1080, 1920
        
        if not vp:
            carb.log_warn("No active viewport window")
            
            self._widget_info_viewport = None
            return
        
        self._login = BitoneBsiSystemLogin(vp, ext_id)
        
    def on_shutdown(self):
        
        if self._login:
            self._login.destroy()
            self._login = None