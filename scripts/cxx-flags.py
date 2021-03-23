#
# common-cxxflags.py
# Convenience script to apply customizations to CPP flags
#
Import("env")
import os


stream = os.popen("date -u +%d/%m/%Y-%H:%M")
output = stream.read()
var = output[:-1]
stream = os.popen("git log --pretty=format:%h -1")
output = stream.read()
var += "_" + output

env.Append(CXXFLAGS=[
    "-DVERSION_STRING=\"%s\"" % var
 # "-Wno-register"
  #"-Wno-incompatible-pointer-types",
  #"-Wno-unused-const-variable",
  #"-Wno-maybe-uninitialized",
  #"-Wno-sign-compare"
])