#!/bin/bash
set -e
prefix="http://agateau.files.wordpress.com"
dst="build/jekyll/agateau.wordpress.com"
egrep -o "$prefix[^\"]*(png|jpe?g)" wordpress-xml/aurlien039sroom.wordpress.2012-02-27.xml | while read url ; do
    name=${url#$prefix}
    if [ ! -e $dst/$name ] ; then
        echo $name
        curl $url > $dst/$name
    fi
done
