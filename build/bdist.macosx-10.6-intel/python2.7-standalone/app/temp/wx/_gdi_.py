
def __load():
    import imp, os, sys
    ext = 'wx/_gdi_.so'
    for path in sys.path:
        print path
        if not path.endswith('lib-dynload'):
            continue
        ext_path = os.path.join(path, ext)
        if os.path.exists(ext_path):
            #print("py2app extension module", __name__, "->", ext_path)
            mod = imp.load_dynamic(__name__, ext_path)
            #mod.frozen = 1
            break
    else:
        raise ImportError(repr(ext) + " not found")
__load()
del __load
