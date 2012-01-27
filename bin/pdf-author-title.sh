#!/bin/sh
if [ -z "$3" ]
then
   # Error message to stderr.
   echo "Usage: `basename $0` <input file> <author> <title>" >&2
   # Returns 65 as exit status of script (error code).
   exit $NOARGS
fi  

pdf-info-change.py "$1" Author "$2"
pdf-info-change.py "$1" Title "$3"
pdfinfo "$1"