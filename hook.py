# encoding: utf-8
import traceback


def exception_hook(exc_type, exc_value, exc_traceback):
    """
    Print the usual traceback information, followed by a listing of all the
    local variables in each frame.
    """
    while True:
        if not exc_traceback.tb_next:
            break
        exc_traceback = exc_traceback.tb_next
    f = exc_traceback.tb_frame
    stack = []
    while f:
        stack.append(f)
        f = f.f_back
    stack.reverse()
    print "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    print "Locals by frame, innermost last"
    for frame in stack:
        print "Frame %s in %s at line %s" % (frame.f_code.co_name,
                                             frame.f_code.co_filename,
                                             frame.f_lineno)
        for key, value in frame.f_locals.items():
            print "\t%20s = " % key,
            try:
                print value
            except:
                print "<ERROR WHILE PRINTING VALUE>"
