from check import is_access_granted

def authenticate(email=None):
    if email is None:
        email = input("# Enter your Email: ")
        
    key = input("# Enter your Auth Key: ")

    if is_access_granted(email, key):
        import sys
        import easyRTML

        # Dynamically import and add to the module's namespace
        from .xg_port import generate_code
        from .pipe import Pipe
        from .pyRTML import pyRTML

        easyRTML.generate_code = generate_code
        easyRTML.Pipe = Pipe
        easyRTML.pyRTML = pyRTML

        return True
    else:
        return False

__all__ = ['authenticate']
