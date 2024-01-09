funkcja = "2*x + 1*x +0 +0 *1 2-0+1"
funkcja = funkcja.replace(" ", "")


def mult1(fcja):
    fcja = fcja.replace("1*", "")
    fcja = fcja.replace("*1", "")
    return fcja

def add0(fcja):
    fcja = fcja.replace("+0", "")
    fcja = fcja.replace("-0", "")
    return fcja

print(mult1(funkcja))