#!/bin/sh
if [ -z "$3" ]
then
   # Error message to stderr.
   echo "Usage: `basename $0` <input file> <author> <title> [year]" >&2
   # Returns 65 as exit status of script (error code).
   exit $NOARGS
fi
  
if [ -z "$4" ]
then
    echo "Year is not supplied." 
else
    pdf-info-change.py "$1" ModDate "D:${4}01010000-00" 
fi

if [ -z "$3" ]
then
    echo "Title is not supplied." 
else
    pdf-info-change.py "$1" Title "$3"
fi

if [ -z "$2" ]
then
    echo "Author is not supplied." 
else
    pdf-info-change.py "$1" Author "$2"
fi

pdfinfo "$1"
