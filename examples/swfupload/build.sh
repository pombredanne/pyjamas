#!/bin/sh

PYJSBUILD="../../bin/pyjsbuild"

options="$*"
#if [ -z $options ] ; then options="-O";fi

COMMAND="$PYJSBUILD --output="html" $options swfu"
echo $COMMAND
$COMMAND 
