#!/bin/bash
set -e
for x in *.markdown ; do
    name=${x/.markdown}
    mkdir $name
    mv $x $name/index.markdown
done
