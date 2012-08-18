# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_wiringpi', [dirname(__file__)])
        except ImportError:
            import _wiringpi
            return _wiringpi
        if fp is not None:
            try:
                _mod = imp.load_module('_wiringpi', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _wiringpi = swig_import_helper()
    del swig_import_helper
else:
    import _wiringpi
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def wiringPiSetup():
  return _wiringpi.wiringPiSetup()
wiringPiSetup = _wiringpi.wiringPiSetup

def wiringPiSetupSys():
  return _wiringpi.wiringPiSetupSys()
wiringPiSetupSys = _wiringpi.wiringPiSetupSys

def wiringPiSetupGpio():
  return _wiringpi.wiringPiSetupGpio()
wiringPiSetupGpio = _wiringpi.wiringPiSetupGpio

def wiringPiGpioMode(*args):
  return _wiringpi.wiringPiGpioMode(*args)
wiringPiGpioMode = _wiringpi.wiringPiGpioMode

def pullUpDnControl(*args):
  return _wiringpi.pullUpDnControl(*args)
pullUpDnControl = _wiringpi.pullUpDnControl

def pinMode(*args):
  return _wiringpi.pinMode(*args)
pinMode = _wiringpi.pinMode

def digitalWrite(*args):
  return _wiringpi.digitalWrite(*args)
digitalWrite = _wiringpi.digitalWrite

def pwmWrite(*args):
  return _wiringpi.pwmWrite(*args)
pwmWrite = _wiringpi.pwmWrite

def digitalRead(*args):
  return _wiringpi.digitalRead(*args)
digitalRead = _wiringpi.digitalRead

def shiftOut(*args):
  return _wiringpi.shiftOut(*args)
shiftOut = _wiringpi.shiftOut

def shiftIn(*args):
  return _wiringpi.shiftIn(*args)
shiftIn = _wiringpi.shiftIn

def delay(*args):
  return _wiringpi.delay(*args)
delay = _wiringpi.delay

def delayMicroseconds(*args):
  return _wiringpi.delayMicroseconds(*args)
delayMicroseconds = _wiringpi.delayMicroseconds

def millis():
  return _wiringpi.millis()
millis = _wiringpi.millis

def serialOpen(*args):
  return _wiringpi.serialOpen(*args)
serialOpen = _wiringpi.serialOpen

def serialClose(*args):
  return _wiringpi.serialClose(*args)
serialClose = _wiringpi.serialClose

def serialPutchar(*args):
  return _wiringpi.serialPutchar(*args)
serialPutchar = _wiringpi.serialPutchar

def serialPuts(*args):
  return _wiringpi.serialPuts(*args)
serialPuts = _wiringpi.serialPuts

def serialDataAvail(*args):
  return _wiringpi.serialDataAvail(*args)
serialDataAvail = _wiringpi.serialDataAvail

def serialGetchar(*args):
  return _wiringpi.serialGetchar(*args)
serialGetchar = _wiringpi.serialGetchar

def serialPrintf(*args):
  return _wiringpi.serialPrintf(*args)
serialPrintf = _wiringpi.serialPrintf
# This file is compatible with both classic and new-style classes.


